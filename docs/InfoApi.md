# lighter.InfoApi

All URIs are relative to *https://mainnet.zklighter.elliot.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layer2_basic_info**](InfoApi.md#layer2_basic_info) | **GET** /api/v1/layer2BasicInfo | layer2BasicInfo


# **layer2_basic_info**
> Layer2BasicInfo layer2_basic_info()

layer2BasicInfo

Get zklighter general info, including contract address, and count of transactions and active users

### Example


```python
import lighter
from lighter.models.layer2_basic_info import Layer2BasicInfo
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
    api_instance = lighter.InfoApi(api_client)

    try:
        # layer2BasicInfo
        api_response = await api_instance.layer2_basic_info()
        print("The response of InfoApi->layer2_basic_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->layer2_basic_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Layer2BasicInfo**](Layer2BasicInfo.md)

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

