# lighter.AccountApi

All URIs are relative to *https://mainnet.zklighter.elliot.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account**](AccountApi.md#account) | **GET** /api/v1/account | account
[**accounts**](AccountApi.md#accounts) | **GET** /api/v1/accounts | accounts
[**accounts_by_l1_address**](AccountApi.md#accounts_by_l1_address) | **GET** /api/v1/accountsByL1Address | accountsByL1Address
[**apikeys**](AccountApi.md#apikeys) | **GET** /api/v1/apikeys | apikeys
[**fee_bucket**](AccountApi.md#fee_bucket) | **GET** /api/v1/feeBucket | feeBucket
[**is_whitelisted**](AccountApi.md#is_whitelisted) | **GET** /api/v1/isWhitelisted | isWhitelisted
[**pnl**](AccountApi.md#pnl) | **GET** /api/v1/pnl | pnl
[**public_pools**](AccountApi.md#public_pools) | **GET** /api/v1/publicPools | publicPools


# **account**
> DetailedAccounts account(by, value)

account

Get account by account's index. <br>More details about account index: [Account Index](https://apidocs.lighter.xyz/docs/account-index)<hr>**Response Description:**<br><br>1) **Status:** 1 is active 0 is inactive.<br>2) **Collateral:** The amount of collateral in the account.<hr>**Position Details Description:**<br>1) **OOC:** Open order count in that market.<br>2) **Sign:** 1 for Long, -1 for Short.<br>3) **Position:** The amount of position in that market.<br>4) **Avg Entry Price:** The average entry price of the position.<br>5) **Position Value:** The value of the position.<br>6) **Unrealized PnL:** The unrealized profit and loss of the position.<br>7) **Realized PnL:** The realized profit and loss of the position.

### Example


```python
import lighter
from lighter.models.detailed_accounts import DetailedAccounts
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    by = 'by_example' # str | 
    value = 'value_example' # str | 

    try:
        # account
        api_response = await api_instance.account(by, value)
        print("The response of AccountApi->account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by** | **str**|  | 
 **value** | **str**|  | 

### Return type

[**DetailedAccounts**](DetailedAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts**
> Accounts accounts(limit, index=index, sort=sort)

accounts

Get accounts returns accounts by account index

### Example


```python
import lighter
from lighter.models.accounts import Accounts
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    limit = 56 # int | 
    index = 56 # int |  (optional)
    sort = asc # str |  (optional) (default to asc)

    try:
        # accounts
        api_response = await api_instance.accounts(limit, index=index, sort=sort)
        print("The response of AccountApi->accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **index** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] [default to asc]

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_by_l1_address**
> SubAccounts accounts_by_l1_address(l1_address)

accountsByL1Address

Get accounts by l1_address returns all accounts associated with the given L1 address

### Example


```python
import lighter
from lighter.models.sub_accounts import SubAccounts
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    l1_address = 'l1_address_example' # str | 

    try:
        # accountsByL1Address
        api_response = await api_instance.accounts_by_l1_address(l1_address)
        print("The response of AccountApi->accounts_by_l1_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->accounts_by_l1_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l1_address** | **str**|  | 

### Return type

[**SubAccounts**](SubAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apikeys**
> AccountApiKeys apikeys(account_index, api_key_index)

apikeys

Get account api key

### Example


```python
import lighter
from lighter.models.account_api_keys import AccountApiKeys
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    account_index = 56 # int | 
    api_key_index = 255 # int |  (default to 255)

    try:
        # apikeys
        api_response = await api_instance.apikeys(account_index, api_key_index)
        print("The response of AccountApi->apikeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apikeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_index** | **int**|  | 
 **api_key_index** | **int**|  | [default to 255]

### Return type

[**AccountApiKeys**](AccountApiKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fee_bucket**
> FeeBucket fee_bucket(account_index)

feeBucket

Get account fee bucket

### Example


```python
import lighter
from lighter.models.fee_bucket import FeeBucket
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    account_index = 56 # int | 

    try:
        # feeBucket
        api_response = await api_instance.fee_bucket(account_index)
        print("The response of AccountApi->fee_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->fee_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_index** | **int**|  | 

### Return type

[**FeeBucket**](FeeBucket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_whitelisted**
> IsWhitelisted is_whitelisted(l1_address)

isWhitelisted

Get is account whitelisted

### Example


```python
import lighter
from lighter.models.is_whitelisted import IsWhitelisted
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    l1_address = 'l1_address_example' # str | 

    try:
        # isWhitelisted
        api_response = await api_instance.is_whitelisted(l1_address)
        print("The response of AccountApi->is_whitelisted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->is_whitelisted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l1_address** | **str**|  | 

### Return type

[**IsWhitelisted**](IsWhitelisted.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pnl**
> AccountPnL pnl(by, value, resolution, start_timestamp, end_timestamp, count_back, ignore_transfers=ignore_transfers)

pnl

Get account PnL chart

### Example


```python
import lighter
from lighter.models.account_pn_l import AccountPnL
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    by = 'by_example' # str | 
    value = 'value_example' # str | 
    resolution = 'resolution_example' # str | 
    start_timestamp = 56 # int | 
    end_timestamp = 56 # int | 
    count_back = 56 # int | 
    ignore_transfers = False # bool |  (optional) (default to False)

    try:
        # pnl
        api_response = await api_instance.pnl(by, value, resolution, start_timestamp, end_timestamp, count_back, ignore_transfers=ignore_transfers)
        print("The response of AccountApi->pnl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->pnl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by** | **str**|  | 
 **value** | **str**|  | 
 **resolution** | **str**|  | 
 **start_timestamp** | **int**|  | 
 **end_timestamp** | **int**|  | 
 **count_back** | **int**|  | 
 **ignore_transfers** | **bool**|  | [optional] [default to False]

### Return type

[**AccountPnL**](AccountPnL.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_pools**
> PublicPools public_pools(index, limit, filter=filter, account_index=account_index)

publicPools

Get public pools

### Example


```python
import lighter
from lighter.models.public_pools import PublicPools
from lighter.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mainnet.zklighter.elliot.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = lighter.Configuration(
    host = "https://mainnet.zklighter.elliot.ai"
)


# Enter a context with an instance of the API client
async with lighter.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lighter.AccountApi(api_client)
    index = 56 # int | 
    limit = 56 # int | 
    filter = 'filter_example' # str |  (optional)
    account_index = 56 # int |  (optional)

    try:
        # publicPools
        api_response = await api_instance.public_pools(index, limit, filter=filter, account_index=account_index)
        print("The response of AccountApi->public_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->public_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**|  | 
 **limit** | **int**|  | 
 **filter** | **str**|  | [optional] 
 **account_index** | **int**|  | [optional] 

### Return type

[**PublicPools**](PublicPools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

