import asyncio
import logging
import lighter

logging.basicConfig(level=logging.DEBUG)

# The API_KEY_PRIVATE_KEY provided belongs to a dummy account registered on Testnet.
# It was generated using the setup_system.py script, and servers as an example.
BASE_URL = "https://testnet.zklighter.elliot.ai"
API_KEY_PRIVATE_KEY = "0xc0a06468a5bbc9a7b785065a8b227a37fdfa18e2b81d51b018cb03ddd99bfbef4b7551f0f0765639"
ACCOUNT_INDEX = 595
API_KEY_INDEX = 1


def trim_exception(e: Exception) -> str:
    return str(e).strip().split("\n")[-1]


async def main():
    client = lighter.SignerClient(
        url=BASE_URL,
        private_key=API_KEY_PRIVATE_KEY,
        account_index=ACCOUNT_INDEX,
        api_key_index=API_KEY_INDEX,
    )

    tx = await client.create_market_order(
        market_index=0,
        client_order_index=0,
        base_amount=1000,  # 0.1 ETH
        avg_execution_price=170000,  # $1700
        is_ask=True,
    )
    print("Create Order Tx:", tx)
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
