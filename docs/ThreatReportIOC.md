# ThreatReportIOC

Indicator of compromise for a threat report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ioc** | **str** | The indicator of compromise. | [optional] 
**type** | **str** | Type of the indicator of compromise | [optional] 

## Example

```python
from stairwell_openapi_client.models.threat_report_ioc import ThreatReportIOC

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatReportIOC from a JSON string
threat_report_ioc_instance = ThreatReportIOC.from_json(json)
# print the JSON string representation of the object
print ThreatReportIOC.to_json()

# convert the object into a dict
threat_report_ioc_dict = threat_report_ioc_instance.to_dict()
# create an instance of ThreatReportIOC from a dict
threat_report_ioc_from_dict = ThreatReportIOC.from_dict(threat_report_ioc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


