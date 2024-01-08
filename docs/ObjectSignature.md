# ObjectSignature

Contains all information known about an object's certificate based signature.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x509_certificates** | [**List[X509Certificate]**](X509Certificate.md) | The x509 certificates embedded within the portable executable. | [optional] 
**pkcs7_verification_result** | **str** | Whether the x509 certificate chain is valid. This may be unknown if the pkcs7 package does not support the file&#39;s encryption scheme. | [optional] 

## Example

```python
from stairwell_openapi_client.models.object_signature import ObjectSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSignature from a JSON string
object_signature_instance = ObjectSignature.from_json(json)
# print the JSON string representation of the object
print ObjectSignature.to_json()

# convert the object into a dict
object_signature_dict = object_signature_instance.to_dict()
# create an instance of ObjectSignature from a dict
object_signature_form_dict = object_signature.from_dict(object_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


