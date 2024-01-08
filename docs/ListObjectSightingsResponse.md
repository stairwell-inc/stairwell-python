# ListObjectSightingsResponse

Response type for ListObjectSightings RPCs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_sightings** | [**List[ObjectSighting]**](ObjectSighting.md) | The sightings from the parent resource. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_object_sightings_response import ListObjectSightingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectSightingsResponse from a JSON string
list_object_sightings_response_instance = ListObjectSightingsResponse.from_json(json)
# print the JSON string representation of the object
print ListObjectSightingsResponse.to_json()

# convert the object into a dict
list_object_sightings_response_dict = list_object_sightings_response_instance.to_dict()
# create an instance of ListObjectSightingsResponse from a dict
list_object_sightings_response_form_dict = list_object_sightings_response.from_dict(list_object_sightings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


