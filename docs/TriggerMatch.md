# TriggerMatch

Contains data as to what object matched and why it matched a particular trigger.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the trigger. | [optional] [readonly] 
**label** | **str** | Label of the created trigger. | [optional] [readonly] 
**create_time** | **datetime** | The time when the match was created. | [optional] [readonly] 
**match_type** | **str** | Type of trigger match. | [optional] [readonly] 
**object_metadata** | [**ObjectMetadata**](ObjectMetadata.md) |  | [optional] 
**object_sightings** | [**List[ObjectSighting]**](ObjectSighting.md) | All sightings data for object that matched. | [optional] [readonly] 
**trigger_condition** | [**TriggerMatchCondition**](TriggerMatchCondition.md) |  | [optional] 

## Example

```python
from stairwell_openapi_client.models.trigger_match import TriggerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerMatch from a JSON string
trigger_match_instance = TriggerMatch.from_json(json)
# print the JSON string representation of the object
print TriggerMatch.to_json()

# convert the object into a dict
trigger_match_dict = trigger_match_instance.to_dict()
# create an instance of TriggerMatch from a dict
trigger_match_from_dict = TriggerMatch.from_dict(trigger_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


