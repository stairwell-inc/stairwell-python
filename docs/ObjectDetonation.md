# ObjectDetonation

ObjectDetonation contains the status of the detonation analysis and if the analysis is complete, information collected while detonating the application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the detonation. | [optional] 
**tags** | **List[str]** | tags are tags extracted from Triage. | [optional] 
**overview** | **str** | overview contains the overview provided by triage. https://pkg.go.dev/github.com/hatching/triage@v1.0.0/types#OverviewReport | [optional] 
**raw_triage_reports** | **Dict[str, str]** | raw triage reports correspond to each individual sandbox run of an object. https://pkg.go.dev/github.com/hatching/triage@v1.0.0/types#TriageReport | [optional] 
**sample_id** | **str** | sample_id is the sampleID returned by Triage identifying the detonation. | [optional] 
**files** | [**List[FileAction]**](FileAction.md) | Files which were accessed during the detonation. | [optional] 
**registry_keys** | [**List[RegistryKeyAction]**](RegistryKeyAction.md) | Registry keys which were read/written/deleted. | [optional] 
**executed_commands** | **List[str]** | Commands which were executed during the detonation | [optional] 
**mutexes** | **List[str]** | Mutexes which were used during the detonation. | [optional] 
**signatures** | **List[str]** | Any malware signatures which are detected during detonation. | [optional] 
**mitre_attack_ttps** | [**List[MitreAttackTTP]**](MitreAttackTTP.md) | Any mitre signatures which are detected during detonation. Mitre TTPs reference: https://attack.mitre.org/techniques/enterprise/ | [optional] 
**created_services** | **List[str]** | List of created serviced during detonation. | [optional] 
**started_services** | **List[str]** | List of started services during detonation. | [optional] 
**dropped_files** | **List[str]** | Dropped child file hashes. | [optional] 
**in_memory_files** | **List[str]** | In-memory child file hashes. | [optional] 
**detections** | [**List[Detection]**](Detection.md) | Detections (malware family, yara, suricata...) | [optional] 

## Example

```python
from stairwell_openapi_client.models.object_detonation import ObjectDetonation

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectDetonation from a JSON string
object_detonation_instance = ObjectDetonation.from_json(json)
# print the JSON string representation of the object
print ObjectDetonation.to_json()

# convert the object into a dict
object_detonation_dict = object_detonation_instance.to_dict()
# create an instance of ObjectDetonation from a dict
object_detonation_from_dict = ObjectDetonation.from_dict(object_detonation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


