# stairwell_openapi_client.IpAddressesApi

All URIs are relative to *https://app.stairwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_addresses_create_comment**](IpAddressesApi.md#ip_addresses_create_comment) | **POST** /v1/ipAddresses/{ipAddress}/comments | CreateComment
[**ip_addresses_create_opinion**](IpAddressesApi.md#ip_addresses_create_opinion) | **POST** /v1/ipAddresses/{ipAddress}/opinions | CreateOpinion
[**ip_addresses_create_tag**](IpAddressesApi.md#ip_addresses_create_tag) | **POST** /v1/ipAddresses/{ipAddress}/tags | CreateTag
[**ip_addresses_delete_tag**](IpAddressesApi.md#ip_addresses_delete_tag) | **DELETE** /v1/ipAddresses/{ipAddress}/tags/{tag} | DeleteTag
[**ip_addresses_get_ip_address_metadata**](IpAddressesApi.md#ip_addresses_get_ip_address_metadata) | **GET** /v1/ipAddresses/{ipAddress}/metadata | GetIpAddressMetadata
[**ip_addresses_get_tag**](IpAddressesApi.md#ip_addresses_get_tag) | **GET** /v1/ipAddresses/{ipAddress}/tags/{tag} | GetTag
[**ip_addresses_list_comments**](IpAddressesApi.md#ip_addresses_list_comments) | **GET** /v1/ipAddresses/{ipAddress}/comments | ListComments
[**ip_addresses_list_opinions**](IpAddressesApi.md#ip_addresses_list_opinions) | **GET** /v1/ipAddresses/{ipAddress}/opinions | ListOpinions
[**ip_addresses_list_tags**](IpAddressesApi.md#ip_addresses_list_tags) | **GET** /v1/ipAddresses/{ipAddress}/tags | ListTags


# **ip_addresses_create_comment**
> Comment ip_addresses_create_comment(ip_address, comment)

CreateComment

Creates a new comment.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.comment import Comment
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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    comment = stairwell_openapi_client.Comment() # Comment | 

    try:
        # CreateComment
        api_response = await api_instance.ip_addresses_create_comment(ip_address, comment)
        print("The response of IpAddressesApi->ip_addresses_create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_create_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

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

# **ip_addresses_create_opinion**
> Opinion ip_addresses_create_opinion(ip_address, opinion)

CreateOpinion

Creates a new opinion.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.opinion import Opinion
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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    opinion = stairwell_openapi_client.Opinion() # Opinion | 

    try:
        # CreateOpinion
        api_response = await api_instance.ip_addresses_create_opinion(ip_address, opinion)
        print("The response of IpAddressesApi->ip_addresses_create_opinion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_create_opinion: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
 **opinion** | [**Opinion**](Opinion.md)|  | 

### Return type

[**Opinion**](Opinion.md)

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

# **ip_addresses_create_tag**
> Tag ip_addresses_create_tag(ip_address, tag)

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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    tag = stairwell_openapi_client.Tag() # Tag | 

    try:
        # CreateTag
        api_response = await api_instance.ip_addresses_create_tag(ip_address, tag)
        print("The response of IpAddressesApi->ip_addresses_create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_create_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
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

# **ip_addresses_delete_tag**
> ip_addresses_delete_tag(ip_address, tag)

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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    tag = 'tag_example' # str | The tag id.

    try:
        # DeleteTag
        await api_instance.ip_addresses_delete_tag(ip_address, tag)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
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

# **ip_addresses_get_ip_address_metadata**
> IpAddressMetadata ip_addresses_get_ip_address_metadata(ip_address)

GetIpAddressMetadata

Gets metadata for a particular IP address.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.ip_address_metadata import IpAddressMetadata
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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.

    try:
        # GetIpAddressMetadata
        api_response = await api_instance.ip_addresses_get_ip_address_metadata(ip_address)
        print("The response of IpAddressesApi->ip_addresses_get_ip_address_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_get_ip_address_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 

### Return type

[**IpAddressMetadata**](IpAddressMetadata.md)

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

# **ip_addresses_get_tag**
> Tag ip_addresses_get_tag(ip_address, tag)

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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    tag = 'tag_example' # str | The tag id.

    try:
        # GetTag
        api_response = await api_instance.ip_addresses_get_tag(ip_address, tag)
        print("The response of IpAddressesApi->ip_addresses_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
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

# **ip_addresses_list_comments**
> ListCommentsResponse ip_addresses_list_comments(ip_address, page_size=page_size, page_token=page_token)

ListComments

Gets the comments for the specified ip address.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_comments_response import ListCommentsResponse
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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    page_size = 56 # int | The maximum number of comments to return. The service may return fewer than this value. If unspecified, at most 100 comments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListComments` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListComments` must match the call that provided the page token. (optional)

    try:
        # ListComments
        api_response = await api_instance.ip_addresses_list_comments(ip_address, page_size=page_size, page_token=page_token)
        print("The response of IpAddressesApi->ip_addresses_list_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_list_comments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
 **page_size** | **int**| The maximum number of comments to return. The service may return fewer than this value. If unspecified, at most 100 comments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListComments&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListComments&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListCommentsResponse**](ListCommentsResponse.md)

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

# **ip_addresses_list_opinions**
> ListOpinionsResponse ip_addresses_list_opinions(ip_address, page_size=page_size, page_token=page_token)

ListOpinions

Gets the opinions for the specified ip address.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_opinions_response import ListOpinionsResponse
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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    page_size = 56 # int | The maximum number of opinions to return. The service may return fewer than this value. If unspecified, at most 100 opinions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListOpinions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListOpinions` must match the call that provided the page token. (optional)

    try:
        # ListOpinions
        api_response = await api_instance.ip_addresses_list_opinions(ip_address, page_size=page_size, page_token=page_token)
        print("The response of IpAddressesApi->ip_addresses_list_opinions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_list_opinions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
 **page_size** | **int**| The maximum number of opinions to return. The service may return fewer than this value. If unspecified, at most 100 opinions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListOpinions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListOpinions&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListOpinionsResponse**](ListOpinionsResponse.md)

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

# **ip_addresses_list_tags**
> ListTagsResponse ip_addresses_list_tags(ip_address, page_size=page_size, page_token=page_token)

ListTags

Gets the tags for the specified ip address.

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
    api_instance = stairwell_openapi_client.IpAddressesApi(api_client)
    ip_address = 'ip_address_example' # str | The ipAddress id.
    page_size = 56 # int | The maximum number of tags to return. The service may return fewer than this value. If unspecified, at most 100 tags will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListTags` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTags` must match the call that provided the page token. (optional)

    try:
        # ListTags
        api_response = await api_instance.ip_addresses_list_tags(ip_address, page_size=page_size, page_token=page_token)
        print("The response of IpAddressesApi->ip_addresses_list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpAddressesApi->ip_addresses_list_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ipAddress id. | 
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

