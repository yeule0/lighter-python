# ReqGetAccountOrders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_index** | **int** |  | 
**market_id** | **int** |  | 
**cursor** | **str** |  | [optional] 
**limit** | **int** |  | 

## Example

```python
from lighter.models.req_get_account_orders import ReqGetAccountOrders

# TODO update the JSON string below
json = "{}"
# create an instance of ReqGetAccountOrders from a JSON string
req_get_account_orders_instance = ReqGetAccountOrders.from_json(json)
# print the JSON string representation of the object
print(ReqGetAccountOrders.to_json())

# convert the object into a dict
req_get_account_orders_dict = req_get_account_orders_instance.to_dict()
# create an instance of ReqGetAccountOrders from a dict
req_get_account_orders_from_dict = ReqGetAccountOrders.from_dict(req_get_account_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


