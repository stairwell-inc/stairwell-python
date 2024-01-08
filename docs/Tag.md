# Tag

Tag represents a key value pairing applied to particular entity. Only one of object, rule or asset may be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the entity. | [optional] [readonly] 
**value** | **str** | value represents the value of the key value pair. | 
**environment** | **str** | the environment in which this tag will live. | 

## Example

```python
from stairwell_openapi_client.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


