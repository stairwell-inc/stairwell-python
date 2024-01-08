# IpAddressMetadata

IpAddress contains metadata relating to a particular IP address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the IP address. | [optional] 
**ip_address** | **str** | Unique set of numbers assigned to each Internet or network device. | [optional] 
**tags** | [**List[Tag]**](Tag.md) | Tags associated with this ip address. | [optional] 

## Example

```python
from stairwell_openapi_client.models.ip_address_metadata import IpAddressMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddressMetadata from a JSON string
ip_address_metadata_instance = IpAddressMetadata.from_json(json)
# print the JSON string representation of the object
print IpAddressMetadata.to_json()

# convert the object into a dict
ip_address_metadata_dict = ip_address_metadata_instance.to_dict()
# create an instance of IpAddressMetadata from a dict
ip_address_metadata_form_dict = ip_address_metadata.from_dict(ip_address_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


