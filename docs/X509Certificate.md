# X509Certificate

A representation of an x509 certificate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | An encoded hash representing the digital signature of the certificate. | [optional] 
**issuer** | **str** | The common name of the issuer of this certificate. | [optional] 
**subject** | **str** | The common name of the subject of this certificate. | [optional] 
**earliest_valid_time** | **datetime** | The earliest time where this certificate is valid. | [optional] 
**latest_valid_time** | **datetime** | The latest time where this certificate is valid. | [optional] 

## Example

```python
from stairwell_openapi_client.models.x509_certificate import X509Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of X509Certificate from a JSON string
x509_certificate_instance = X509Certificate.from_json(json)
# print the JSON string representation of the object
print X509Certificate.to_json()

# convert the object into a dict
x509_certificate_dict = x509_certificate_instance.to_dict()
# create an instance of X509Certificate from a dict
x509_certificate_form_dict = x509_certificate.from_dict(x509_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


