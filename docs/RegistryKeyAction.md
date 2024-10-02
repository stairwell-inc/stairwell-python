# RegistryKeyAction

RegistryKeyActions define the registry keys which were accessed/modified during detonation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_key** | **str** | The registry key path | [optional] 
**action** | **str** | Action performed on the registry key | [optional] 
**registry_key_hive** | **str** | Logical group of keys, subkeys, and values related to the registry key | [optional] 

## Example

```python
from stairwell_openapi_client.models.registry_key_action import RegistryKeyAction

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryKeyAction from a JSON string
registry_key_action_instance = RegistryKeyAction.from_json(json)
# print the JSON string representation of the object
print RegistryKeyAction.to_json()

# convert the object into a dict
registry_key_action_dict = registry_key_action_instance.to_dict()
# create an instance of RegistryKeyAction from a dict
registry_key_action_from_dict = RegistryKeyAction.from_dict(registry_key_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


