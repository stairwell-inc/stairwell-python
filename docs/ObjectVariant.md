# ObjectVariant

Contains metadata about an object and its similarity score to the original.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**ObjectMetadata**](ObjectMetadata.md) |  | [optional] 
**similarity** | **float** | The similarity to the origin file in terms of a percentage. | [optional] 

## Example

```python
from stairwell_openapi_client.models.object_variant import ObjectVariant

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectVariant from a JSON string
object_variant_instance = ObjectVariant.from_json(json)
# print the JSON string representation of the object
print ObjectVariant.to_json()

# convert the object into a dict
object_variant_dict = object_variant_instance.to_dict()
# create an instance of ObjectVariant from a dict
object_variant_from_dict = ObjectVariant.from_dict(object_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


