# FileAction

FileActions define the files which were accessed/modified during detonation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Path to the file | [optional] 
**action** | **str** | Action performed on the file | [optional] 

## Example

```python
from stairwell_openapi_client.models.file_action import FileAction

# TODO update the JSON string below
json = "{}"
# create an instance of FileAction from a JSON string
file_action_instance = FileAction.from_json(json)
# print the JSON string representation of the object
print FileAction.to_json()

# convert the object into a dict
file_action_dict = file_action_instance.to_dict()
# create an instance of FileAction from a dict
file_action_from_dict = FileAction.from_dict(file_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


