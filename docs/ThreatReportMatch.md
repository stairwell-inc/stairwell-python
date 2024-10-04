# ThreatReportMatch

ThreatReportMatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_metadata** | [**ObjectMetadata**](ObjectMetadata.md) |  | [optional] 

## Example

```python
from stairwell_openapi_client.models.threat_report_match import ThreatReportMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatReportMatch from a JSON string
threat_report_match_instance = ThreatReportMatch.from_json(json)
# print the JSON string representation of the object
print ThreatReportMatch.to_json()

# convert the object into a dict
threat_report_match_dict = threat_report_match_instance.to_dict()
# create an instance of ThreatReportMatch from a dict
threat_report_match_from_dict = ThreatReportMatch.from_dict(threat_report_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


