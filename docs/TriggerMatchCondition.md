# TriggerMatchCondition

Condition of the trigger which matched the object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yara_rule_match** | **List[str]** | Yara rule names which triggered a match . | [optional] 
**mal_eval** | [**MalEval**](MalEval.md) |  | [optional] 
**opinion** | [**Opinion**](Opinion.md) |  | [optional] 
**threat_reports** | [**List[ThreatReport]**](ThreatReport.md) | Threat reports that triggered a match. | [optional] 

## Example

```python
from stairwell_openapi_client.models.trigger_match_condition import TriggerMatchCondition

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerMatchCondition from a JSON string
trigger_match_condition_instance = TriggerMatchCondition.from_json(json)
# print the JSON string representation of the object
print TriggerMatchCondition.to_json()

# convert the object into a dict
trigger_match_condition_dict = trigger_match_condition_instance.to_dict()
# create an instance of TriggerMatchCondition from a dict
trigger_match_condition_from_dict = TriggerMatchCondition.from_dict(trigger_match_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


