# Comment

Comment represents a key value pairing applied to particular entity. Only one of object, rule or asset may be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The body of the comment. | 
**email** | **str** | The email of the user who made the comment. | [optional] [readonly] 
**create_time** | **datetime** | The time when the comment was added. | [optional] [readonly] 
**environment** | **str** | the environment in which this tag will live. | 

## Example

```python
from stairwell_openapi_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print Comment.to_json()

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_form_dict = comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


