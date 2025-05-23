import ctypes
import json
import platform
import logging
import os
import time

from eth_account import Account
from eth_account.messages import encode_defunct
from pydantic import StrictInt
import lighter
from lighter.configuration import Configuration
from lighter.models import TxHash
from lighter.transactions import CreateOrder, CancelOrder, Withdraw

logging.basicConfig(level=logging.DEBUG)


class ApiKeyResponse(ctypes.Structure):
    _fields_ = [("privateKey", ctypes.c_char_p), ("publicKey", ctypes.c_char_p), ("err", ctypes.c_char_p)]


class StrOrErr(ctypes.Structure):
    _fields_ = [("str", ctypes.c_char_p), ("err", ctypes.c_char_p)]


def _initialize_signer():
    is_linux = platform.system() == "Linux"
    is_mac = platform.system() == "Darwin"
    is_x64 = platform.machine().lower() in ("amd64", "x86_64")
    is_arm = platform.machine().lower() == "arm64"

    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    path_to_signer_folders = os.path.join(current_file_directory, "signers")

    if is_arm and is_mac:
        logging.debug("Detected ARM architecture on macOS.")
        return ctypes.CDLL(os.path.join(path_to_signer_folders, "signer-arm64.dylib"))
    elif is_linux and is_x64:
        logging.debug("Detected x64/amd architecture on Linux.")
        return ctypes.CDLL(os.path.join(path_to_signer_folders, "signer-amd64.so"))
    else:
        raise Exception(
            f"Unsupported platform/architecture: {platform.system()}/{platform.machine()} only supports Linux(x86) and Darwin(arm64)"
        )


def create_api_key(seed=""):
    signer = _initialize_signer()
    signer.GenerateAPIKey.argtypes = [
        ctypes.c_char_p,
    ]
    signer.GenerateAPIKey.restype = ApiKeyResponse
    result = signer.GenerateAPIKey(ctypes.c_char_p(seed.encode("utf-8")))

    private_key_str = result.privateKey.decode("utf-8") if result.privateKey else None
    public_key_str = result.publicKey.decode("utf-8") if result.publicKey else None
    error = result.err.decode("utf-8") if result.err else None

    return private_key_str, public_key_str, error


class SignerClient:
    USDC_TICKER_SCALE = 1e6

    TX_TYPE_CHANGE_PUB_KEY = 8
    TX_TYPE_CREATE_SUB_ACCOUNT = 9
    TX_TYPE_CREATE_PUBLIC_POOL = 10
    TX_TYPE_UPDATE_PUBLIC_POOL = 11
    TX_TYPE_TRANSFER = 12
    TX_TYPE_WITHDRAW = 13
    TX_TYPE_CREATE_ORDER = 14
    TX_TYPE_CANCEL_ORDER = 15
    TX_TYPE_CANCEL_ALL_ORDERS = 16
    TX_TYPE_MODIFY_ORDER = 17
    TX_TYPE_MINT_SHARES = 18
    TX_TYPE_BURN_SHARES = 19

    ORDER_TYPE_LIMIT = 0
    ORDER_TYPE_MARKET = 1
    ORDER_TYPE_STOP_LOSS = 2
    ORDER_TYPE_STOP_LOSS_LIMIT = 3
    ORDER_TYPE_TAKE_PROFIT = 4
    ORDER_TYPE_TAKE_PROFIT_LIMIT = 5
    ORDER_TYPE_TWAP = 6

    ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL = 0
    ORDER_TIME_IN_FORCE_GOOD_TILL_TIME = 1
    ORDER_TIME_IN_FORCE_POST_ONLY = 2

    NIL_TRIGGER_PRICE = 0
    DEFAULT_28_DAY_ORDER_EXPIRY = -1
    DEFAULT_IOC_EXPIRY = 0
    DEFAULT_10_MIN_AUTH_EXPIRY = -1
    MINUTE = 60

    def __init__(self, url, private_key, api_key_index, account_index):
        chain_id = 304 if "mainnet" in url else 300

        # api_key_index=0 is generally used by frontend
        if private_key.startswith("0x"):
            private_key = private_key[2:]
        self.url = url
        self.private_key = private_key
        self.chain_id = chain_id
        self.api_key_index = api_key_index
        self.account_index = account_index
        self.signer = _initialize_signer()
        self.api_client = lighter.ApiClient(configuration=Configuration(host=url))
        self.tx_api = lighter.TransactionApi(self.api_client)
        self.create_client()

    def create_client(self):
        self.signer.CreateClient.argtypes = [
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_longlong,
        ]
        self.signer.CreateClient.restype = ctypes.c_char_p
        err = self.signer.CreateClient(
            self.url.encode("utf-8"),
            self.private_key.encode("utf-8"),
            self.chain_id,
            self.api_key_index,
            self.account_index,
        )

        if err is None:
            return

        err_str = err.decode("utf-8")
        raise Exception(err_str)

    # check_client verifies that the given API key associated with (api_key_index, account_index) matches the one on Lighter
    def check_client(self):
        self.signer.CheckClient.argtypes = [
            ctypes.c_int,
            ctypes.c_longlong,
        ]
        self.signer.CheckClient.restype = ctypes.c_char_p

        result = self.signer.CheckClient(self.api_key_index, self.account_index)
        return result.decode("utf-8") if result else None

    def create_api_key(self, seed=""):
        self.signer.GenerateAPIKey.argtypes = [
            ctypes.c_char_p,
        ]
        self.signer.GenerateAPIKey.restype = ApiKeyResponse
        result = self.signer.GenerateAPIKey(ctypes.c_char_p(seed.encode("utf-8")))

        private_key_str = result.str.decode("utf-8") if result.privateKey else None
        public_key_str = result.str.decode("utf-8") if result.publicKey else None
        error = result.err.decode("utf-8") if result.err else None

        return private_key_str, public_key_str, error

    def sign_change_api_key(self, eth_private_key, new_pubkey: str, nonce: int):
        self.signer.SignChangePubKey.argtypes = [
            ctypes.c_char_p,
            ctypes.c_longlong,
        ]
        self.signer.SignChangePubKey.restype = StrOrErr
        result = self.signer.SignChangePubKey(ctypes.c_char_p(new_pubkey.encode("utf-8")), nonce)

        tx_info_str = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None
        if error is not None:
            return None, error

        # fetch message to sign
        tx_info = json.loads(tx_info_str)
        msg_to_sign = tx_info["MessageToSign"]
        del tx_info["MessageToSign"]

        # sign the message
        acct = Account.from_key(eth_private_key)
        message = encode_defunct(text=msg_to_sign)
        signature = acct.sign_message(message)
        tx_info["L1Sig"] = signature.signature.to_0x_hex()
        return json.dumps(tx_info), None

    def sign_create_order(
        self,
        market_index,
        client_order_index,
        base_amount,
        price,
        is_ask,
        order_type,
        time_in_force,
        reduce_only,
        trigger_price,
        order_expiry=DEFAULT_28_DAY_ORDER_EXPIRY,
        nonce=-1,
    ):
        self.signer.SignCreateOrder.argtypes = [
            ctypes.c_int,
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignCreateOrder.restype = StrOrErr

        result = self.signer.SignCreateOrder(
            market_index,
            client_order_index,
            base_amount,
            price,
            int(is_ask),
            order_type,
            time_in_force,
            reduce_only,
            trigger_price,
            order_expiry,
            nonce,
        )

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_cancel_order(self, market_index, order_index, nonce=-1):
        self.signer.SignCancelOrder.argtypes = [
            ctypes.c_int,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignCancelOrder.restype = StrOrErr

        result = self.signer.SignCancelOrder(market_index, order_index, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_withdraw(self, usdc_amount, nonce=-1):
        self.signer.SignWithdraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
        self.signer.SignWithdraw.restype = StrOrErr

        result = self.signer.SignWithdraw(usdc_amount, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_create_sub_account(self, nonce=-1):
        self.signer.SignCreateSubAccount.argtypes = [ctypes.c_longlong]
        self.signer.SignCreateSubAccount.restype = StrOrErr

        result = self.signer.SignCreateSubAccount(nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_cancel_all_orders(self, time_in_force, time, nonce=-1):
        self.signer.SignCancelAllOrders.argtypes = [
            ctypes.c_int,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignCancelAllOrders.restype = StrOrErr

        result = self.signer.SignCancelAllOrders(time_in_force, time, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_modify_order(self, market_index, order_index, base_amount, price, trigger_price, nonce=-1):
        self.signer.SignModifyOrder.argtypes = [
            ctypes.c_int,
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignModifyOrder.restype = StrOrErr

        result = self.signer.SignModifyOrder(market_index, order_index, base_amount, price, trigger_price, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_transfer(self, to_account_index, usdc_amount, nonce=-1):
        self.signer.SignTransfer.argtypes = [
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignTransfer.restype = StrOrErr

        result = self.signer.SignTransfer(to_account_index, usdc_amount, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_create_public_pool(self, operator_fee, initial_total_shares, min_operator_share_rate, nonce=-1):
        self.signer.SignCreatePublicPool.argtypes = [
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignCreatePublicPool.restype = StrOrErr

        result = self.signer.SignCreatePublicPool(operator_fee, initial_total_shares, min_operator_share_rate, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_update_public_pool(self, public_pool_index, status, operator_fee, min_operator_share_rate, nonce=-1):
        self.signer.SignUpdatePublicPool.argtypes = [
            ctypes.c_longlong,
            ctypes.c_int,
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignUpdatePublicPool.restype = StrOrErr

        result = self.signer.SignUpdatePublicPool(
            public_pool_index, status, operator_fee, min_operator_share_rate, nonce
        )

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_mint_shares(self, public_pool_index, share_amount, nonce=-1):
        self.signer.SignMintShares.argtypes = [
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignMintShares.restype = StrOrErr

        result = self.signer.SignMintShares(public_pool_index, share_amount, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_burn_shares(self, public_pool_index, share_amount, nonce=-1):
        self.signer.SignBurnShares.argtypes = [
            ctypes.c_longlong,
            ctypes.c_longlong,
            ctypes.c_longlong,
        ]
        self.signer.SignBurnShares.restype = StrOrErr

        result = self.signer.SignBurnShares(public_pool_index, share_amount, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def sign_update_leverage(self, market_index, leverage, nonce=-1):
        self.signer.SignUpdateLeverage.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_longlong,
        ]
        self.signer.SignUpdateLeverage.restype = StrOrErr

        result = self.signer.SignUpdateLeverage(market_index, leverage, nonce)

        tx_info = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return tx_info, error

    def create_auth_token_with_expiry(self, deadline: int = DEFAULT_10_MIN_AUTH_EXPIRY):
        if deadline == SignerClient.DEFAULT_10_MIN_AUTH_EXPIRY:
            deadline = int(time.time() + 10 * SignerClient.MINUTE)
        self.signer.CreateAuthToken.argtypes = [ctypes.c_longlong]
        self.signer.CreateAuthToken.restype = StrOrErr

        result = self.signer.CreateAuthToken(deadline)

        auth = result.str.decode("utf-8") if result.str else None
        error = result.err.decode("utf-8") if result.err else None

        return auth, error

    async def change_api_key(self, eth_private_key: str, new_pubkey: str, nonce=-1):
        tx_info, error = self.sign_change_api_key(eth_private_key, new_pubkey, nonce)
        if error is not None:
            return None, error

        logging.debug(f"Change Pub Key Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_CHANGE_PUB_KEY, tx_info=tx_info)
        logging.debug(f"Change Pub Key Send Tx Response: {api_response}")
        return api_response, None

    async def create_order(
        self,
        market_index,
        client_order_index,
        base_amount,
        price,
        is_ask,
        order_type,
        time_in_force,
        reduce_only=False,
        trigger_price=NIL_TRIGGER_PRICE,
        order_expiry=-1,
        nonce=-1,
    ) -> (CreateOrder, TxHash, str):
        tx_info, error = self.sign_create_order(
            market_index,
            client_order_index,
            base_amount,
            price,
            int(is_ask),
            order_type,
            time_in_force,
            int(reduce_only),
            trigger_price,
            order_expiry,
            nonce,
        )
        if error is not None:
            return None, None, error
        logging.debug(f"Create Order Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_CREATE_ORDER, tx_info=tx_info)
        logging.debug(f"Create Order Send Tx Response: {api_response}")
        return CreateOrder.from_json(tx_info), api_response, None

    async def create_market_order(
        self, market_index, client_order_index, base_amount, avg_execution_price, is_ask, reduce_only: bool = False
    ) -> (CreateOrder, TxHash, str):
        return await self.create_order(
            market_index,
            client_order_index,
            base_amount,
            avg_execution_price,
            is_ask,
            order_type=self.ORDER_TYPE_MARKET,
            time_in_force=self.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
            order_expiry=self.DEFAULT_IOC_EXPIRY,
            reduce_only=reduce_only,
        )

    async def cancel_order(self, market_index, order_index, nonce=-1) -> (CancelOrder, TxHash, str):
        tx_info, error = self.sign_cancel_order(market_index, order_index, nonce)
        if error is not None:
            return None, None, error
        logging.debug(f"Cancel Order Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_CANCEL_ORDER, tx_info=tx_info)
        logging.debug(f"Cancel Order Send Tx Response: {api_response}")
        return CancelOrder.from_json(tx_info), api_response, None

    async def withdraw(self, usdc_amount, nonce=-1) -> (Withdraw, TxHash):
        usdc_amount = int(usdc_amount * self.USDC_TICKER_SCALE)

        tx_info, error = self.sign_withdraw(usdc_amount, nonce)
        if error is not None:
            return None, None, error
        logging.debug(f"Withdraw Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_WITHDRAW, tx_info=tx_info)
        logging.debug(f"Withdraw Send Tx Response: {api_response}")
        return Withdraw.from_json(tx_info), api_response, None

    async def create_sub_account(self, nonce=-1):
        tx_info, error = self.sign_create_sub_account(nonce)
        if error is not None:
            return None, error
        logging.debug(f"Create Sub Account Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_CREATE_SUB_ACCOUNT, tx_info=tx_info)
        logging.debug(f"Create Sub Account Send Tx Response: {api_response}")
        return api_response, None

    async def cancel_all_orders(self, time_in_force, time, nonce=-1):
        tx_info, error = self.sign_cancel_all_orders(time_in_force, time, nonce)
        if error is not None:
            return None, error
        logging.debug(f"Cancel All Orders Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_CANCEL_ALL_ORDERS, tx_info=tx_info)
        logging.debug(f"Cancel All Orders Send Tx Response: {api_response}")
        return api_response, None

    async def modify_order(self, market_index, order_index, base_amount, price, trigger_price, nonce=-1):
        tx_info, error = self.sign_modify_order(market_index, order_index, base_amount, price, trigger_price, nonce)
        if error is not None:
            return None, error
        logging.debug(f"Modify Order Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_MODIFY_ORDER, tx_info=tx_info)
        logging.debug(f"Modify Order Send Tx Response: {api_response}")
        return api_response, None

    async def transfer(self, to_account_index, usdc_amount, nonce=-1):
        usdc_amount = int(usdc_amount * self.USDC_TICKER_SCALE)

        tx_info, error = self.sign_transfer(to_account_index, usdc_amount, nonce)
        if error is not None:
            return None, error
        logging.debug(f"Transfer Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_TRANSFER, tx_info=tx_info)
        logging.debug(f"Transfer Send Tx Response: {api_response}")
        return api_response, None

    async def create_public_pool(self, operator_fee, initial_total_shares, min_operator_share_rate, nonce=-1):
        tx_info, error = self.sign_create_public_pool(
            operator_fee, initial_total_shares, min_operator_share_rate, nonce
        )
        if error is not None:
            return None, error
        logging.debug(f"Create Public Pool Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_CREATE_PUBLIC_POOL, tx_info=tx_info)
        logging.debug(f"Create Public Pool Send Tx Response: {api_response}")
        return api_response, None

    async def update_public_pool(self, public_pool_index, status, operator_fee, min_operator_share_rate, nonce=-1):
        tx_info, error = self.sign_update_public_pool(
            public_pool_index, status, operator_fee, min_operator_share_rate, nonce
        )
        if error is not None:
            return None, error
        logging.debug(f"Update Public Pool Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_UPDATE_PUBLIC_POOL, tx_info=tx_info)
        logging.debug(f"Update Public Pool Send Tx Response: {api_response}")
        return api_response, None

    async def mint_shares(self, public_pool_index, share_amount, nonce=-1):
        tx_info, error = self.sign_mint_shares(public_pool_index, share_amount, nonce)
        if error is not None:
            return None, error
        logging.debug(f"Mint Shares Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_MINT_SHARES, tx_info=tx_info)
        logging.debug(f"Mint Shares Send Tx Response: {api_response}")
        return api_response, None

    async def burn_shares(self, public_pool_index, share_amount, nonce=-1):
        tx_info, error = self.sign_burn_shares(public_pool_index, share_amount, nonce)
        if error is not None:
            return None, error
        logging.debug(f"Burn Shares Tx Info: {tx_info}")

        api_response = await self.send_tx(tx_type=self.TX_TYPE_BURN_SHARES, tx_info=tx_info)
        logging.debug(f"Burn Shares Send Tx Response: {api_response}")
        return api_response, None

    async def send_tx(self, tx_type: StrictInt, tx_info: str) -> TxHash:
        if tx_info[0] != "{":
            raise Exception(tx_info)
        return await self.tx_api.send_tx(tx_type=tx_type, tx_info=tx_info)

    async def close(self):
        await self.api_client.close()
