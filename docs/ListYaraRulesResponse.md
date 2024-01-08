# ListYaraRulesResponse

ListYaraRulesResponse contains a list of rules and the next page token.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yara_rules** | [**List[YaraRule]**](YaraRule.md) | The rules from the parent resource. | [optional] 
**next_page_token** | **str** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 

## Example

```python
from stairwell_openapi_client.models.list_yara_rules_response import ListYaraRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListYaraRulesResponse from a JSON string
list_yara_rules_response_instance = ListYaraRulesResponse.from_json(json)
# print the JSON string representation of the object
print ListYaraRulesResponse.to_json()

# convert the object into a dict
list_yara_rules_response_dict = list_yara_rules_response_instance.to_dict()
# create an instance of ListYaraRulesResponse from a dict
list_yara_rules_response_form_dict = list_yara_rules_response.from_dict(list_yara_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


