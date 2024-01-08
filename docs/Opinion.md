# Opinion

Opinion represents a key value pairing applied to particular entity. Only one of object, rule or asset may be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** | The opinion put on the entity. | 
**environment** | **str** | Environment the opinion is set in | 
**email** | **str** | The email of the user who made the opinion. | [optional] [readonly] 
**create_time** | **datetime** | The time when the opinion was added. | [optional] [readonly] 

## Example

```python
from stairwell_openapi_client.models.opinion import Opinion

# TODO update the JSON string below
json = "{}"
# create an instance of Opinion from a JSON string
opinion_instance = Opinion.from_json(json)
# print the JSON string representation of the object
print Opinion.to_json()

# convert the object into a dict
opinion_dict = opinion_instance.to_dict()
# create an instance of Opinion from a dict
opinion_form_dict = opinion.from_dict(opinion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


