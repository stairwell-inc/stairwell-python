# HostnameMetadata

HostnameMetadata contains metadata relating to a hostname.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the hostname. | 
**hostname** | **str** | Hostname examples are - hurirk.net - www.tcoolonline.mobi - www.crackedmindstechnologies.com | 
**a_records** | [**List[DNSLookupResult]**](DNSLookupResult.md) | A records (IPv4). | [optional] 
**aaaa_records** | [**List[DNSLookupResult]**](DNSLookupResult.md) | AAAA records (IPv6). | [optional] 
**mx_records** | [**List[DNSLookupResult]**](DNSLookupResult.md) | MX records. | [optional] 
**tags** | [**List[Tag]**](Tag.md) | Tags associated with this hostname. | [optional] [readonly] 

## Example

```python
from stairwell_openapi_client.models.hostname_metadata import HostnameMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of HostnameMetadata from a JSON string
hostname_metadata_instance = HostnameMetadata.from_json(json)
# print the JSON string representation of the object
print HostnameMetadata.to_json()

# convert the object into a dict
hostname_metadata_dict = hostname_metadata_instance.to_dict()
# create an instance of HostnameMetadata from a dict
hostname_metadata_form_dict = hostname_metadata.from_dict(hostname_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


