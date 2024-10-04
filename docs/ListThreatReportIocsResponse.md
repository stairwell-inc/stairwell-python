# ListThreatReportIocsResponse

ListThreatReportIocsResponse is the response message for ListThreatReportIocs RPC.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_report_iocs** | [**List[ThreatReportIOC]**](ThreatReportIOC.md) | The hashes which are part of the threat report. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_threat_report_iocs_response import ListThreatReportIocsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListThreatReportIocsResponse from a JSON string
list_threat_report_iocs_response_instance = ListThreatReportIocsResponse.from_json(json)
# print the JSON string representation of the object
print ListThreatReportIocsResponse.to_json()

# convert the object into a dict
list_threat_report_iocs_response_dict = list_threat_report_iocs_response_instance.to_dict()
# create an instance of ListThreatReportIocsResponse from a dict
list_threat_report_iocs_response_from_dict = ListThreatReportIocsResponse.from_dict(list_threat_report_iocs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


