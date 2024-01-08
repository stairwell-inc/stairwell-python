# ObjectMetadata

ObjectMetadata contains static and extracted metadata relating to an object (file).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name of the object. | [optional] 
**md5** | **str** | md5 is the md5 hash signature of an object. | [optional] 
**sha1** | **str** | sha1 is the sha1 hash signature of an object. | [optional] 
**sha256** | **str** | sha256 is the sha256 hash signature of an object. | [optional] 
**sha3256** | **str** | sha3256 is the sha3_256 hash signature of an object. | [optional] 
**size** | **str** | size is the size of the file in bytes. | [optional] 
**stairwell_first_seen_time** | **datetime** | stairwell_first_seen_time is the timestamp at which an object was first observed by Stairwell. | [optional] 
**tags** | [**List[Tag]**](Tag.md) | Tags associated with this object. Currently only populated by GetObjectMetadata. Other endpoints returning objects omit this field. | [optional] 
**detonation** | [**ObjectDetonation**](ObjectDetonation.md) |  | [optional] 
**mal_eval** | [**MalEval**](MalEval.md) |  | [optional] 
**environments** | **List[str]** | List of environments that this object has been seen within. | [optional] 
**yara_rule_matches** | **List[str]** | Yara rule resource names which have matched on this object. If more than 1000 yara rule, the matches will be truncated. | [optional] 
**network_indicators** | [**NetworkIndicators**](NetworkIndicators.md) |  | [optional] 
**magic** | **str** | Magic number as determined by yara rule based identification. | [optional] 
**mime_type** | **str** | MIME type as determined by yara rule based identification. | [optional] 
**shannon_entropy** | **float** | Measure of the information contained in a object as opposed to the portion of the object that is determined (or predictable). | [optional] 
**imphash** | **str** | The Mandiant import hash (imphash) of the object. | [optional] 
**imphash_sorted** | **str** | The sorted import hash (imphash) of the object where the imports are sorted. | [optional] 
**tlsh** | **str** | The TLSH of the object, see https://github.com/trendmicro/tlsh | [optional] 
**object_signature** | [**ObjectSignature**](ObjectSignature.md) |  | [optional] 

## Example

```python
from stairwell_openapi_client.models.object_metadata import ObjectMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMetadata from a JSON string
object_metadata_instance = ObjectMetadata.from_json(json)
# print the JSON string representation of the object
print ObjectMetadata.to_json()

# convert the object into a dict
object_metadata_dict = object_metadata_instance.to_dict()
# create an instance of ObjectMetadata from a dict
object_metadata_form_dict = object_metadata.from_dict(object_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


