# ThreatReport

ThreatReport is a intelligence source that contains threat information about entities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the entity. | [optional] 
**uid** | **str** | ID of the threat report of the form six characters of base62. | [readonly] 
**environment** | **str** | Environment that contains the threat report. | 
**title** | **str** | Title of the threat report. | [optional] [readonly] 
**upload_time** | **datetime** | When the threat report was uploaded. | [optional] [readonly] 
**sources** | **List[str]** | Sources, for example the organization, that the threat report came from. | [optional] 
**description** | **str** | Automatically generated summarization of the threat report | [optional] 
**report_uri** | **str** | URI of the original report. | 

## Example

```python
from stairwell_openapi_client.models.threat_report import ThreatReport

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatReport from a JSON string
threat_report_instance = ThreatReport.from_json(json)
# print the JSON string representation of the object
print ThreatReport.to_json()

# convert the object into a dict
threat_report_dict = threat_report_instance.to_dict()
# create an instance of ThreatReport from a dict
threat_report_from_dict = ThreatReport.from_dict(threat_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


