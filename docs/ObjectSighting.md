# ObjectSighting

A sighting of an object on a particular asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sighting_time** | **datetime** | The timestamp at which the object was observed on the asset. | [optional] 
**environment** | **str** | Environment in which the asset resides. | [optional] 
**asset** | **str** | Asset resource name which the object was sighted on. | [optional] 
**filename** | **str** | Name of file on disk. | [optional] 
**filepath** | **str** | Path to file on disk. | [optional] 
**asset_name** | **str** | Name of the asset. | [optional] 
**parent_sha256** | **str** | Optional parent SHA265 if the object was packed. | [optional] 

## Example

```python
from stairwell_openapi_client.models.object_sighting import ObjectSighting

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSighting from a JSON string
object_sighting_instance = ObjectSighting.from_json(json)
# print the JSON string representation of the object
print ObjectSighting.to_json()

# convert the object into a dict
object_sighting_dict = object_sighting_instance.to_dict()
# create an instance of ObjectSighting from a dict
object_sighting_from_dict = ObjectSighting.from_dict(object_sighting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


