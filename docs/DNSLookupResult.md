# DNSLookupResult

This represents result of a DNS lookup.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | DNS lookup state | [optional] [readonly] 
**address** | **str** | Address the hostname resolved to at lookup time. | [optional] 
**lookup_time** | **datetime** | Time is the time the lookup was made. | [optional] 

## Example

```python
from stairwell_openapi_client.models.dns_lookup_result import DNSLookupResult

# TODO update the JSON string below
json = "{}"
# create an instance of DNSLookupResult from a JSON string
dns_lookup_result_instance = DNSLookupResult.from_json(json)
# print the JSON string representation of the object
print DNSLookupResult.to_json()

# convert the object into a dict
dns_lookup_result_dict = dns_lookup_result_instance.to_dict()
# create an instance of DNSLookupResult from a dict
dns_lookup_result_form_dict = dns_lookup_result.from_dict(dns_lookup_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


