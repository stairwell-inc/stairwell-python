# ListTriggerMatchesResponse

ListTriggerMatchesResponse contains a list of trigger matches and an optional next page token.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_matches** | [**List[TriggerMatch]**](TriggerMatch.md) | The trigger matches from the given environment. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_trigger_matches_response import ListTriggerMatchesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTriggerMatchesResponse from a JSON string
list_trigger_matches_response_instance = ListTriggerMatchesResponse.from_json(json)
# print the JSON string representation of the object
print ListTriggerMatchesResponse.to_json()

# convert the object into a dict
list_trigger_matches_response_dict = list_trigger_matches_response_instance.to_dict()
# create an instance of ListTriggerMatchesResponse from a dict
list_trigger_matches_response_from_dict = ListTriggerMatchesResponse.from_dict(list_trigger_matches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


