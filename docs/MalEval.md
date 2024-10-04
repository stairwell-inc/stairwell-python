# MalEval

Malware Evaluation result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | Labels derived from the malware evalation. | [optional] 
**probability_bucket** | **str** | Confidence that the label applies on the object. | [optional] 
**severity** | **str** | Severity of malware detected. | [optional] 

## Example

```python
from stairwell_openapi_client.models.mal_eval import MalEval

# TODO update the JSON string below
json = "{}"
# create an instance of MalEval from a JSON string
mal_eval_instance = MalEval.from_json(json)
# print the JSON string representation of the object
print MalEval.to_json()

# convert the object into a dict
mal_eval_dict = mal_eval_instance.to_dict()
# create an instance of MalEval from a dict
mal_eval_from_dict = MalEval.from_dict(mal_eval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


