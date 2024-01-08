# ListObjectVariantsResponse

Response type for ListObjectVariants RPCs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_variants** | [**List[ObjectVariant]**](ObjectVariant.md) | The variants from the parent resource. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_object_variants_response import ListObjectVariantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectVariantsResponse from a JSON string
list_object_variants_response_instance = ListObjectVariantsResponse.from_json(json)
# print the JSON string representation of the object
print ListObjectVariantsResponse.to_json()

# convert the object into a dict
list_object_variants_response_dict = list_object_variants_response_instance.to_dict()
# create an instance of ListObjectVariantsResponse from a dict
list_object_variants_response_form_dict = list_object_variants_response.from_dict(list_object_variants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


