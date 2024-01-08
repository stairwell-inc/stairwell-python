# MitreAttackTTP

MitreAttackTTP contains the MITRE signatures which were observed during detonation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttp** | **str** | TTP is a code indicating the signature which was observed. Code reference: https://attack.mitre.org/techniques/enterprise/ | [optional] 
**signature** | **str** | Signature is the name of the signature which was observed. | [optional] 

## Example

```python
from stairwell_openapi_client.models.mitre_attack_ttp import MitreAttackTTP

# TODO update the JSON string below
json = "{}"
# create an instance of MitreAttackTTP from a JSON string
mitre_attack_ttp_instance = MitreAttackTTP.from_json(json)
# print the JSON string representation of the object
print MitreAttackTTP.to_json()

# convert the object into a dict
mitre_attack_ttp_dict = mitre_attack_ttp_instance.to_dict()
# create an instance of MitreAttackTTP from a dict
mitre_attack_ttp_form_dict = mitre_attack_ttp.from_dict(mitre_attack_ttp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


