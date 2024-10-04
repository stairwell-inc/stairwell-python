# ListThreatReportMatchesResponse

ListThreatReportMatchesResponse is the response message for ListThreatReportMatches RPC.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_report_matches** | [**List[ThreatReportMatch]**](ThreatReportMatch.md) | The objects matching the specified filter. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_threat_report_matches_response import ListThreatReportMatchesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListThreatReportMatchesResponse from a JSON string
list_threat_report_matches_response_instance = ListThreatReportMatchesResponse.from_json(json)
# print the JSON string representation of the object
print ListThreatReportMatchesResponse.to_json()

# convert the object into a dict
list_threat_report_matches_response_dict = list_threat_report_matches_response_instance.to_dict()
# create an instance of ListThreatReportMatchesResponse from a dict
list_threat_report_matches_response_from_dict = ListThreatReportMatchesResponse.from_dict(list_threat_report_matches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


