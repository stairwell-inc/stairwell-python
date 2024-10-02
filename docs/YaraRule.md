# YaraRule

YaraRule contains metadata and definition of a particular rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the rule. | [optional] 
**definition** | **str** | Definition of the rule. | 
**scan_warning** | **str** | Warning from a failed canary scan. | [optional] [readonly] 
**state** | **str** | Current scan inclusion state of rule. | [optional] [readonly] 
**update_time** | **datetime** | Timestamp at which the latest rule version was submitted. | [optional] [readonly] 
**canary_scan_state** | **str** | State from running this rule against known goodware. | [optional] [readonly] 
**tags** | [**List[Tag]**](Tag.md) | Tags associated with this yara rule. | [optional] 

## Example

```python
from stairwell_openapi_client.models.yara_rule import YaraRule

# TODO update the JSON string below
json = "{}"
# create an instance of YaraRule from a JSON string
yara_rule_instance = YaraRule.from_json(json)
# print the JSON string representation of the object
print YaraRule.to_json()

# convert the object into a dict
yara_rule_dict = yara_rule_instance.to_dict()
# create an instance of YaraRule from a dict
yara_rule_from_dict = YaraRule.from_dict(yara_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


