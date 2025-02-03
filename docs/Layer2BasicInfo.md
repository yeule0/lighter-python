# Layer2BasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**message** | **str** |  | [optional] 
**block_committed** | **int** |  | 
**block_verified** | **int** |  | 
**total_transaction_count** | **int** |  | 

## Example

```python
from lighter.models.layer2_basic_info import Layer2BasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Layer2BasicInfo from a JSON string
layer2_basic_info_instance = Layer2BasicInfo.from_json(json)
# print the JSON string representation of the object
print(Layer2BasicInfo.to_json())

# convert the object into a dict
layer2_basic_info_dict = layer2_basic_info_instance.to_dict()
# create an instance of Layer2BasicInfo from a dict
layer2_basic_info_from_dict = Layer2BasicInfo.from_dict(layer2_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


