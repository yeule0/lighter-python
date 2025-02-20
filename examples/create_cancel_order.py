import asyncio
import logging
import time
from lighter import SignerClient
import lighter
import lighter.configuration

logging.basicConfig(level=logging.DEBUG)


BASE_URL = "https://testnet.zklighter.elliot.ai"
PRIVATE_KEY = "WALLET_PRIVATE_KEY"


def trim_exception(e: Exception) -> str:
    return str(e).strip().split("\n")[-1]


async def main():
    api_client = lighter.ApiClient(
        configuration=lighter.Configuration(host=BASE_URL)
    )

    # assuring that client is created
    account_created = False
    new_account = False
    while not account_created:
        try:
            client = SignerClient(url=BASE_URL, private_key=PRIVATE_KEY)
            await client.set_account_index()
            account_created = True
            if new_account:
                time.sleep(10)
        except Exception as e:
            new_account = True
            print("Account not created yet", trim_exception(e))
        time.sleep(2)
        
    print("Account Index: ", client.account_index)

    tx = await client.create_order(
        market_index=0,
        client_order_index=0,
        base_amount=10000,
        price=250000,
        is_ask=False,
        order_type=lighter.SignerClient.ORDER_TYPE_LIMIT,
        time_in_force=lighter.SignerClient.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
        reduce_only=0,
        trigger_price=0,
    )
    print("Create Order Tx:", tx)

    auth = client.create_auth_token_with_expiry(SignerClient.DEFAULT_10_MIN_AUTH_EXPIRY)
    print("Auth:", auth)

    active_orders = await lighter.OrderApi(api_client).account_active_orders(
        account_index=client.account_index, market_id=0, auth=auth
    )
    if len(active_orders.orders) == 0:
        print("No active orders")
        return

    print("Active Orders:", active_orders.orders)

    last_order_index = active_orders.orders[0].order_index

    tx, response = await client.cancel_order(
        market_index=0, order_index=last_order_index
    )
    print(
        f"code: {response.code} msg: {response.message} l2Hash: {response.tx_hash} tx: {tx.to_json()}"
    )

    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())
