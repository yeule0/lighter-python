import asyncio
import logging
from lighter import SignerClient
import lighter

logging.basicConfig(level=logging.DEBUG)


BASE_URL = "https://mainnet.zklighter.elliot.ai"
PRIVATE_KEY = "WALLET_PRIVATE_KEY"


async def main():
    api_client = lighter.ApiClient()
    client = SignerClient(url=BASE_URL, private_key=PRIVATE_KEY)
    await client.set_account_index()
    print("Account Index: ", client.account_index)

    tx = await client.create_order(
        market_index=0,
        client_order_index=0,
        base_amount=100000,
        price=250000,
        is_ask=0,
        order_type=lighter.SignerClient.ORDER_TYPE_LIMIT,
        time_in_force=lighter.SignerClient.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
        reduce_only=0,
        trigger_price=0,
    )
    print("Create Order Tx:", tx)

    auth = client.create_auth_token()
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
