import asyncio
import datetime
import lighter
import logging

logging.basicConfig(level=logging.INFO)


async def print_api(method, *args, **kwargs):
    logging.info(f"{method.__name__}: {await method(*args, **kwargs)}")


async def account_apis(client: lighter.ApiClient):
    logging.info("ACCOUNT APIS")
    account_instance = lighter.AccountApi(client)
    await print_api(account_instance.account, by="index", value="3")
    await print_api(account_instance.accounts, index=0, limit=2, sort="asc")
    await print_api(
        account_instance.accounts_by_l1_address,
        l1_address="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    )
    # await print_api(account_instance.apikeys, account_index=3, api_key_index=255)
    await print_api(account_instance.fee_bucket, account_index=3)
    await print_api(
        account_instance.is_whitelisted,
        l1_address="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    )
    await print_api(
        account_instance.pnl,
        by="index",
        value="1",
        resolution="1h",
        start_timestamp=int(datetime.datetime.now().timestamp() - 60 * 60 * 24),
        end_timestamp=int(datetime.datetime.now().timestamp()),
        count_back=2,
    )
    await print_api(account_instance.public_pools, filter="all", limit=1, index=0)


async def block_apis(client: lighter.ApiClient):
    logging.info("BLOCK APIS")
    block_instance = lighter.BlockApi(client)
    await print_api(block_instance.block, by="height", value="1")
    await print_api(block_instance.blocks, index=0, limit=2, sort="asc")
    await print_api(block_instance.current_height)


async def candlestick_apis(client: lighter.ApiClient):
    logging.info("CANDLESTICK APIS")
    candlestick_instance = lighter.CandlestickApi(client)
    await print_api(
        candlestick_instance.candlesticks,
        market_id=0,
        resolution="1h",
        start_timestamp=int(datetime.datetime.now().timestamp() - 60 * 60 * 24),
        end_timestamp=int(datetime.datetime.now().timestamp()),
        count_back=2,
    )
    await print_api(
        candlestick_instance.fundings,
        market_id=0,
        resolution="1h",
        start_timestamp=int(datetime.datetime.now().timestamp() - 60 * 60 * 24),
        end_timestamp=int(datetime.datetime.now().timestamp()),
        count_back=2,
    )


async def info_apis(client: lighter.ApiClient):
    logging.info("INFO APIS")
    info_instance = lighter.InfoApi(client)
    await print_api(info_instance.layer1_basic_info)
    await print_api(info_instance.layer2_basic_info)


async def order_apis(client: lighter.ApiClient):
    logging.info("ORDER APIS")
    order_instance = lighter.OrderApi(client)
    # TODO: Add auth to sharedlib
    # await print_api(
    #     order_instance.account_active_orders,
    #     account_index=3,
    #     market_id=0,
    # )
    await print_api(
        order_instance.account_inactive_orders,
        account_index=3,
        market_id=0,
        limit=2,
    )
    await print_api(
        order_instance.account_orders, account_index=3, market_id=0, limit=2
    )
    await print_api(order_instance.exchange_stats)
    await print_api(order_instance.order_book_details, market_id=0)
    await print_api(order_instance.order_book_orders, market_id=0, limit=2)
    await print_api(order_instance.order_books)
    await print_api(order_instance.recent_trades, market_id=0, limit=2)
    await print_api(order_instance.trades, sort_by="timestamp", market_id=0, limit=2)


async def transaction_apis(client: lighter.ApiClient):
    logging.info("TRANSACTION APIS")
    transaction_instance = lighter.TransactionApi(client)
    # await print_api(
    #     transaction_instance.account_pending_txs,
    #     by="account_index",
    #     value="3",
    # )
    await print_api(
        transaction_instance.account_txs,
        by="account_index",
        value="0",
        index=0,
        limit=2,
    )
    await print_api(transaction_instance.block_txs, by="block_height", value="1")
    await print_api(
        transaction_instance.deposit_history,
        l1_address="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    )
    await print_api(transaction_instance.next_nonce, account_index=1, api_key_index=0)
    # await print_api(transaction_instance.pending_txs, limit=2)
    await print_api(transaction_instance.tx, by="sequence_index", value="5")
    # await print_api(transaction_instance.tx_from_l1_tx_hash, hash="0x")
    await print_api(transaction_instance.txs, index=0, limit=2)
    await print_api(transaction_instance.withdraw_history, account_index=3)


async def main():
    client = lighter.ApiClient(
        configuration=lighter.Configuration(host="https://staging.lighter.elliot.ai")
    )
    await account_apis(client)
    await block_apis(client)
    await candlestick_apis(client)
    await info_apis(client)
    await order_apis(client)
    await transaction_apis(client)


if __name__ == "__main__":
    asyncio.run(main())
