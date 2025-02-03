# WithdrawHistoryCursor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secure_id** | **str** |  | 
**fast_id** | **str** |  | 

## Example

```python
from lighter.models.withdraw_history_cursor import WithdrawHistoryCursor

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawHistoryCursor from a JSON string
withdraw_history_cursor_instance = WithdrawHistoryCursor.from_json(json)
# print the JSON string representation of the object
print(WithdrawHistoryCursor.to_json())

# convert the object into a dict
withdraw_history_cursor_dict = withdraw_history_cursor_instance.to_dict()
# create an instance of WithdrawHistoryCursor from a dict
withdraw_history_cursor_from_dict = WithdrawHistoryCursor.from_dict(withdraw_history_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


