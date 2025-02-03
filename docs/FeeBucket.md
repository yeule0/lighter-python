# FeeBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vip_tier** | **int** |  | 
**taker_fee** | **int** |  | 
**maker_fee** | **int** |  | 

## Example

```python
from lighter.models.fee_bucket import FeeBucket

# TODO update the JSON string below
json = "{}"
# create an instance of FeeBucket from a JSON string
fee_bucket_instance = FeeBucket.from_json(json)
# print the JSON string representation of the object
print(FeeBucket.to_json())

# convert the object into a dict
fee_bucket_dict = fee_bucket_instance.to_dict()
# create an instance of FeeBucket from a dict
fee_bucket_from_dict = FeeBucket.from_dict(fee_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


