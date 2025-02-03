# IsWhitelisted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**message** | **str** |  | [optional] 
**whitelisted** | **bool** |  | 
**deposit_amount_left** | **str** |  | 

## Example

```python
from lighter.models.is_whitelisted import IsWhitelisted

# TODO update the JSON string below
json = "{}"
# create an instance of IsWhitelisted from a JSON string
is_whitelisted_instance = IsWhitelisted.from_json(json)
# print the JSON string representation of the object
print(IsWhitelisted.to_json())

# convert the object into a dict
is_whitelisted_dict = is_whitelisted_instance.to_dict()
# create an instance of IsWhitelisted from a dict
is_whitelisted_from_dict = IsWhitelisted.from_dict(is_whitelisted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


