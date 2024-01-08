# stairwell_openapi_client.YaraRulesApi

All URIs are relative to *https://app.stairwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**yara_rules_create_tag**](YaraRulesApi.md#yara_rules_create_tag) | **POST** /v1/environments/{environment}/yaraRules/{yaraRule}/tags | CreateTag
[**yara_rules_create_yara_rule**](YaraRulesApi.md#yara_rules_create_yara_rule) | **POST** /v1/environments/{environment}/yaraRules | CreateYaraRule
[**yara_rules_delete_tag**](YaraRulesApi.md#yara_rules_delete_tag) | **DELETE** /v1/environments/{environment}/yaraRules/{yaraRule}/tags/{tag} | DeleteTag
[**yara_rules_delete_yara_rule**](YaraRulesApi.md#yara_rules_delete_yara_rule) | **DELETE** /v1/environments/{environment}/yaraRules/{yaraRule} | DeleteYaraRule
[**yara_rules_get_tag**](YaraRulesApi.md#yara_rules_get_tag) | **GET** /v1/environments/{environment}/yaraRules/{yaraRule}/tags/{tag} | GetTag
[**yara_rules_get_yara_rule**](YaraRulesApi.md#yara_rules_get_yara_rule) | **GET** /v1/environments/{environment}/yaraRules/{yaraRule} | GetYaraRule
[**yara_rules_list_tags**](YaraRulesApi.md#yara_rules_list_tags) | **GET** /v1/environments/{environment}/yaraRules/{yaraRule}/tags | ListTags
[**yara_rules_list_yara_rules**](YaraRulesApi.md#yara_rules_list_yara_rules) | **GET** /v1/environments/{environment}/yaraRules | ListYaraRules
[**yara_rules_update_yara_rule**](YaraRulesApi.md#yara_rules_update_yara_rule) | **PATCH** /v1/environments/{environment}/yaraRules/{yaraRule} | UpdateYaraRule


# **yara_rules_create_tag**
> Tag yara_rules_create_tag(environment, yara_rule, tag)

CreateTag

Creates a new tag.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.tag import Tag
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.
    tag = stairwell_openapi_client.Tag() # Tag | 

    try:
        # CreateTag
        api_response = await api_instance.yara_rules_create_tag(environment, yara_rule, tag)
        print("The response of YaraRulesApi->yara_rules_create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_create_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 
 **tag** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_create_yara_rule**
> YaraRule yara_rules_create_yara_rule(environment, yara_rule)

CreateYaraRule

Gets metadata and rule definition.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.yara_rule import YaraRule
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = stairwell_openapi_client.YaraRule() # YaraRule | 

    try:
        # CreateYaraRule
        api_response = await api_instance.yara_rules_create_yara_rule(environment, yara_rule)
        print("The response of YaraRulesApi->yara_rules_create_yara_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_create_yara_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | [**YaraRule**](YaraRule.md)|  | 

### Return type

[**YaraRule**](YaraRule.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_delete_tag**
> yara_rules_delete_tag(environment, yara_rule, tag)

DeleteTag

Deletes a tag.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.
    tag = 'tag_example' # str | The tag id.

    try:
        # DeleteTag
        await api_instance.yara_rules_delete_tag(environment, yara_rule, tag)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 
 **tag** | **str**| The tag id. | 

### Return type

void (empty response body)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_delete_yara_rule**
> yara_rules_delete_yara_rule(environment, yara_rule, force=force)

DeleteYaraRule

Gets metadata and rule definition.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.
    force = True # bool | Force deletion even if tags exist (optional)

    try:
        # DeleteYaraRule
        await api_instance.yara_rules_delete_yara_rule(environment, yara_rule, force=force)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_delete_yara_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 
 **force** | **bool**| Force deletion even if tags exist | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_get_tag**
> Tag yara_rules_get_tag(environment, yara_rule, tag)

GetTag

Gets a specified tag by name.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.tag import Tag
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.
    tag = 'tag_example' # str | The tag id.

    try:
        # GetTag
        api_response = await api_instance.yara_rules_get_tag(environment, yara_rule, tag)
        print("The response of YaraRulesApi->yara_rules_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 
 **tag** | **str**| The tag id. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_get_yara_rule**
> YaraRule yara_rules_get_yara_rule(environment, yara_rule)

GetYaraRule

Gets metadata and rule definition.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.yara_rule import YaraRule
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.

    try:
        # GetYaraRule
        api_response = await api_instance.yara_rules_get_yara_rule(environment, yara_rule)
        print("The response of YaraRulesApi->yara_rules_get_yara_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_get_yara_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 

### Return type

[**YaraRule**](YaraRule.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_list_tags**
> ListTagsResponse yara_rules_list_tags(environment, yara_rule, page_size=page_size, page_token=page_token)

ListTags

Gets the tags for the specified yara rule.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_tags_response import ListTagsResponse
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.
    page_size = 56 # int | The maximum number of tags to return. The service may return fewer than this value. If unspecified, at most 100 tags will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListTags` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTags` must match the call that provided the page token. (optional)

    try:
        # ListTags
        api_response = await api_instance.yara_rules_list_tags(environment, yara_rule, page_size=page_size, page_token=page_token)
        print("The response of YaraRulesApi->yara_rules_list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_list_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 
 **page_size** | **int**| The maximum number of tags to return. The service may return fewer than this value. If unspecified, at most 100 tags will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListTags&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListTags&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_list_yara_rules**
> ListYaraRulesResponse yara_rules_list_yara_rules(environment, page_size=page_size, page_token=page_token)

ListYaraRules

Gets metadata and rule definition.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_yara_rules_response import ListYaraRulesResponse
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    page_size = 56 # int | The number of yara rules to return in a single page (optional)
    page_token = 'page_token_example' # str | The page token for getting successive pages (optional)

    try:
        # ListYaraRules
        api_response = await api_instance.yara_rules_list_yara_rules(environment, page_size=page_size, page_token=page_token)
        print("The response of YaraRulesApi->yara_rules_list_yara_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_list_yara_rules: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **page_size** | **int**| The number of yara rules to return in a single page | [optional] 
 **page_token** | **str**| The page token for getting successive pages | [optional] 

### Return type

[**ListYaraRulesResponse**](ListYaraRulesResponse.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yara_rules_update_yara_rule**
> YaraRule yara_rules_update_yara_rule(environment, yara_rule, yara_rule2, update_mask=update_mask)

UpdateYaraRule

Gets metadata and rule definition.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.yara_rule import YaraRule
from stairwell_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.stairwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stairwell_openapi_client.Configuration(
    host = "https://app.stairwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthToken
configuration.api_key['AuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with stairwell_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stairwell_openapi_client.YaraRulesApi(api_client)
    environment = 'environment_example' # str | The environment id.
    yara_rule = 'yara_rule_example' # str | The yaraRule id.
    yara_rule2 = stairwell_openapi_client.YaraRule() # YaraRule | 
    update_mask = 'update_mask_example' # str | The fields of the yara rule to update. Currently supports status and definition. (optional)

    try:
        # UpdateYaraRule
        api_response = await api_instance.yara_rules_update_yara_rule(environment, yara_rule, yara_rule2, update_mask=update_mask)
        print("The response of YaraRulesApi->yara_rules_update_yara_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YaraRulesApi->yara_rules_update_yara_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **yara_rule** | **str**| The yaraRule id. | 
 **yara_rule2** | [**YaraRule**](YaraRule.md)|  | 
 **update_mask** | **str**| The fields of the yara rule to update. Currently supports status and definition. | [optional] 

### Return type

[**YaraRule**](YaraRule.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

