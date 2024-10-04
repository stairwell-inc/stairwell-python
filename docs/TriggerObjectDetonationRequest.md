# TriggerObjectDetonationRequest

Request for the TriggerObjectDetonationRequest RPC.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** | The parent resource where this detonation will be triggered. | 

## Example

```python
from stairwell_openapi_client.models.trigger_object_detonation_request import TriggerObjectDetonationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerObjectDetonationRequest from a JSON string
trigger_object_detonation_request_instance = TriggerObjectDetonationRequest.from_json(json)
# print the JSON string representation of the object
print TriggerObjectDetonationRequest.to_json()

# convert the object into a dict
trigger_object_detonation_request_dict = trigger_object_detonation_request_instance.to_dict()
# create an instance of TriggerObjectDetonationRequest from a dict
trigger_object_detonation_request_from_dict = TriggerObjectDetonationRequest.from_dict(trigger_object_detonation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


