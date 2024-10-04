# ListTagsResponse

Response type for ListTags RPCs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) | The tags from the parent resource. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_tags_response import ListTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTagsResponse from a JSON string
list_tags_response_instance = ListTagsResponse.from_json(json)
# print the JSON string representation of the object
print ListTagsResponse.to_json()

# convert the object into a dict
list_tags_response_dict = list_tags_response_instance.to_dict()
# create an instance of ListTagsResponse from a dict
list_tags_response_from_dict = ListTagsResponse.from_dict(list_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


