# ReqGetAccountPendingTxs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**types** | **List[int]** |  | [optional] 

## Example

```python
from lighter.models.req_get_account_pending_txs import ReqGetAccountPendingTxs

# TODO update the JSON string below
json = "{}"
# create an instance of ReqGetAccountPendingTxs from a JSON string
req_get_account_pending_txs_instance = ReqGetAccountPendingTxs.from_json(json)
# print the JSON string representation of the object
print(ReqGetAccountPendingTxs.to_json())

# convert the object into a dict
req_get_account_pending_txs_dict = req_get_account_pending_txs_instance.to_dict()
# create an instance of ReqGetAccountPendingTxs from a dict
req_get_account_pending_txs_from_dict = ReqGetAccountPendingTxs.from_dict(req_get_account_pending_txs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


