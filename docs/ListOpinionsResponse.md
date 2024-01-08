# ListOpinionsResponse

Response type for ListOpinions RPCs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opinions** | [**List[Opinion]**](Opinion.md) | The opinions from the parent resource. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_opinions_response import ListOpinionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOpinionsResponse from a JSON string
list_opinions_response_instance = ListOpinionsResponse.from_json(json)
# print the JSON string representation of the object
print ListOpinionsResponse.to_json()

# convert the object into a dict
list_opinions_response_dict = list_opinions_response_instance.to_dict()
# create an instance of ListOpinionsResponse from a dict
list_opinions_response_form_dict = list_opinions_response.from_dict(list_opinions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


