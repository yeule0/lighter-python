# Trade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **int** |  | 
**tx_hash** | **str** |  | 
**type** | **str** |  | 
**market_id** | **int** |  | 
**size** | **str** |  | 
**price** | **str** |  | 
**usd_amount** | **str** |  | 
**ask_id** | **int** |  | 
**bid_id** | **int** |  | 
**ask_account_id** | **int** |  | 
**bid_account_id** | **int** |  | 
**is_maker_ask** | **bool** |  | 
**block_height** | **int** |  | 
**timestamp** | **int** |  | 

## Example

```python
from lighter.models.trade import Trade

# TODO update the JSON string below
json = "{}"
# create an instance of Trade from a JSON string
trade_instance = Trade.from_json(json)
# print the JSON string representation of the object
print(Trade.to_json())

# convert the object into a dict
trade_dict = trade_instance.to_dict()
# create an instance of Trade from a dict
trade_from_dict = Trade.from_dict(trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


