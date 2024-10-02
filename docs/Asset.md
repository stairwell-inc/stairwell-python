# Asset

Asset represents any entity (usually a machine) which uploads objects to the Stairwell platform.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the asset. | [optional] 
**label** | **str** | Label of the asset. | [optional] 
**create_time** | **datetime** | Creation time of the asset. | [optional] [readonly] 
**last_checkin_time** | **datetime** | Last time the asset made an RPC into the platform. | [optional] [readonly] 
**environment** | **str** | Environment that this asset lives in. | [optional] [readonly] 
**forwarder_version** | **str** | Forwarder version of the form {major}.{minor}.{patch} | [optional] [readonly] 
**mac_address** | **str** | The media access control address specific to this asset. | [optional] [readonly] 
**os** | **str** | Operating system running on this asset. | [optional] [readonly] 
**os_version** | **str** | Operating system version of the form {major}.{minor}.{patch} | [optional] [readonly] 
**tags** | [**List[Tag]**](Tag.md) | Tags associated with this asset. | [optional] [readonly] 
**upload_token** | **str** | Private authorization id and token for uploading to the asset | [optional] [readonly] 

## Example

```python
from stairwell_openapi_client.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print Asset.to_json()

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


