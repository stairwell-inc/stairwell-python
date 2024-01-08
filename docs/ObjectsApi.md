# stairwell_openapi_client.ObjectsApi

All URIs are relative to *https://app.stairwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**objects_create_comment**](ObjectsApi.md#objects_create_comment) | **POST** /v1/objects/{object}/comments | CreateComment
[**objects_create_opinion**](ObjectsApi.md#objects_create_opinion) | **POST** /v1/objects/{object}/opinions | CreateOpinion
[**objects_create_tag**](ObjectsApi.md#objects_create_tag) | **POST** /v1/objects/{object}/tags | CreateTag
[**objects_delete_tag**](ObjectsApi.md#objects_delete_tag) | **DELETE** /v1/objects/{object}/tags/{tag} | DeleteTag
[**objects_download_object**](ObjectsApi.md#objects_download_object) | **GET** /v1/objects/{object}:download | DownloadObject
[**objects_get_object_detonation**](ObjectsApi.md#objects_get_object_detonation) | **GET** /v1/objects/{object}/detonation | GetObjectDetonation
[**objects_get_object_metadata**](ObjectsApi.md#objects_get_object_metadata) | **GET** /v1/objects/{object}/metadata | GetObjectMetadata
[**objects_get_tag**](ObjectsApi.md#objects_get_tag) | **GET** /v1/objects/{object}/tags/{tag} | GetTag
[**objects_list_comments**](ObjectsApi.md#objects_list_comments) | **GET** /v1/objects/{object}/comments | ListComments
[**objects_list_object_metadata**](ObjectsApi.md#objects_list_object_metadata) | **GET** /v1/objects/metadata | ListObjectMetadata
[**objects_list_object_sightings**](ObjectsApi.md#objects_list_object_sightings) | **GET** /v1/objects/{object}/sightings | ListObjectSightings
[**objects_list_object_variants**](ObjectsApi.md#objects_list_object_variants) | **GET** /v1/objects/{object}/variants | ListObjectVariants
[**objects_list_opinions**](ObjectsApi.md#objects_list_opinions) | **GET** /v1/objects/{object}/opinions | ListOpinions
[**objects_list_tags**](ObjectsApi.md#objects_list_tags) | **GET** /v1/objects/{object}/tags | ListTags
[**objects_trigger_object_detonation**](ObjectsApi.md#objects_trigger_object_detonation) | **POST** /v1/objects/{object}/detonation:trigger | TriggerObjectDetonation


# **objects_create_comment**
> Comment objects_create_comment(object, comment)

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    comment = stairwell_openapi_client.Comment() # Comment | 

    try:
        # CreateComment
        api_response = await api_instance.objects_create_comment(object, comment)
        print("The response of ObjectsApi->objects_create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_create_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_create_opinion**
> Opinion objects_create_opinion(object, opinion)

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    opinion = stairwell_openapi_client.Opinion() # Opinion | 

    try:
        # CreateOpinion
        api_response = await api_instance.objects_create_opinion(object, opinion)
        print("The response of ObjectsApi->objects_create_opinion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_create_opinion: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_create_tag**
> Tag objects_create_tag(object, tag)

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    tag = stairwell_openapi_client.Tag() # Tag | 

    try:
        # CreateTag
        api_response = await api_instance.objects_create_tag(object, tag)
        print("The response of ObjectsApi->objects_create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_create_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_delete_tag**
> objects_delete_tag(object, tag)

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    tag = 'tag_example' # str | The tag id.

    try:
        # DeleteTag
        await api_instance.objects_delete_tag(object, tag)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_download_object**
> objects_download_object(object)

DownloadObject

Downloads the object as file.

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.

    try:
        # DownloadObject
        await api_instance.objects_download_object(object)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_download_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 

### Return type

void (empty response body)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objects_get_object_detonation**
> ObjectDetonation objects_get_object_detonation(object)

GetObjectDetonation

Gets a specified detonation by name.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.object_detonation import ObjectDetonation
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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.

    try:
        # GetObjectDetonation
        api_response = await api_instance.objects_get_object_detonation(object)
        print("The response of ObjectsApi->objects_get_object_detonation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_get_object_detonation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 

### Return type

[**ObjectDetonation**](ObjectDetonation.md)

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

# **objects_get_object_metadata**
> ObjectMetadata objects_get_object_metadata(object)

GetObjectMetadata

Gets the metadata for the object specified.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.object_metadata import ObjectMetadata
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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.

    try:
        # GetObjectMetadata
        api_response = await api_instance.objects_get_object_metadata(object)
        print("The response of ObjectsApi->objects_get_object_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_get_object_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 

### Return type

[**ObjectMetadata**](ObjectMetadata.md)

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

# **objects_get_tag**
> Tag objects_get_tag(object, tag)

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    tag = 'tag_example' # str | The tag id.

    try:
        # GetTag
        api_response = await api_instance.objects_get_tag(object, tag)
        print("The response of ObjectsApi->objects_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_list_comments**
> ListCommentsResponse objects_list_comments(object, page_size=page_size, page_token=page_token)

ListComments

Gets the comments for the specified object.

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    page_size = 56 # int | The maximum number of comments to return. The service may return fewer than this value. If unspecified, at most 100 comments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListComments` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListComments` must match the call that provided the page token. (optional)

    try:
        # ListComments
        api_response = await api_instance.objects_list_comments(object, page_size=page_size, page_token=page_token)
        print("The response of ObjectsApi->objects_list_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list_comments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_list_object_metadata**
> ListObjectMetadataResponse objects_list_object_metadata(filter=filter, page_size=page_size, page_token=page_token)

ListObjectMetadata

Fetches a list of object metadata. Objects returned match the filter  specified in the request.   https://help.stairwell.com/en/knowledge/how-do-i-write-a-cel-query

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_object_metadata_response import ListObjectMetadataResponse
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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    filter = 'filter_example' # str | CEL string filter which objects must match. https://help.stairwell.com/en/knowledge/how-do-i-write-a-cel-query (optional)
    page_size = 56 # int | The maximum number of objects to return. The service may return fewer than this value. If unspecified, at most 50 objects will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListObjectMetadata` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListObjectMetadata` must match the call that provided the page token. (optional)

    try:
        # ListObjectMetadata
        api_response = await api_instance.objects_list_object_metadata(filter=filter, page_size=page_size, page_token=page_token)
        print("The response of ObjectsApi->objects_list_object_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list_object_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| CEL string filter which objects must match. https://help.stairwell.com/en/knowledge/how-do-i-write-a-cel-query | [optional] 
 **page_size** | **int**| The maximum number of objects to return. The service may return fewer than this value. If unspecified, at most 50 objects will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListObjectMetadata&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListObjectMetadata&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListObjectMetadataResponse**](ListObjectMetadataResponse.md)

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

# **objects_list_object_sightings**
> ListObjectSightingsResponse objects_list_object_sightings(object, page_size=page_size, page_token=page_token)

ListObjectSightings

Gets the sightings for the specified object an any assets on which it has  appeared.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_object_sightings_response import ListObjectSightingsResponse
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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    page_size = 56 # int | The maximum number of sightings to return. The service may return fewer than this value. If unspecified, at most 100 sightings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListObjectSightings` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListObjectSightings` must match the call that provided the page token. (optional)

    try:
        # ListObjectSightings
        api_response = await api_instance.objects_list_object_sightings(object, page_size=page_size, page_token=page_token)
        print("The response of ObjectsApi->objects_list_object_sightings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list_object_sightings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
 **page_size** | **int**| The maximum number of sightings to return. The service may return fewer than this value. If unspecified, at most 100 sightings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListObjectSightings&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListObjectSightings&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListObjectSightingsResponse**](ListObjectSightingsResponse.md)

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

# **objects_list_object_variants**
> ListObjectVariantsResponse objects_list_object_variants(object, page_size=page_size, page_token=page_token)

ListObjectVariants

Gets the variants for the specified object.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_object_variants_response import ListObjectVariantsResponse
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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    page_size = 56 # int | The maximum number of variants to return. The service may return fewer than this value. If unspecified, at most 100 variants will be returned. The maximum value is 100; values above 100 will be coerced to 100. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListObjectVariants` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListObjectVariants` must match the call that provided the page token. (optional)

    try:
        # ListObjectVariants
        api_response = await api_instance.objects_list_object_variants(object, page_size=page_size, page_token=page_token)
        print("The response of ObjectsApi->objects_list_object_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list_object_variants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
 **page_size** | **int**| The maximum number of variants to return. The service may return fewer than this value. If unspecified, at most 100 variants will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListObjectVariants&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListObjectVariants&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListObjectVariantsResponse**](ListObjectVariantsResponse.md)

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

# **objects_list_opinions**
> ListOpinionsResponse objects_list_opinions(object, page_size=page_size, page_token=page_token)

ListOpinions

Gets the opinions for the specified object.

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    page_size = 56 # int | The maximum number of opinions to return. The service may return fewer than this value. If unspecified, at most 100 opinions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListOpinions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListOpinions` must match the call that provided the page token. (optional)

    try:
        # ListOpinions
        api_response = await api_instance.objects_list_opinions(object, page_size=page_size, page_token=page_token)
        print("The response of ObjectsApi->objects_list_opinions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list_opinions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_list_tags**
> ListTagsResponse objects_list_tags(object, page_size=page_size, page_token=page_token)

ListTags

Gets the tags for the specified object.

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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    page_size = 56 # int | The maximum number of tags to return. The service may return fewer than this value. If unspecified, at most 100 tags will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListTags` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTags` must match the call that provided the page token. (optional)

    try:
        # ListTags
        api_response = await api_instance.objects_list_tags(object, page_size=page_size, page_token=page_token)
        print("The response of ObjectsApi->objects_list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
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

# **objects_trigger_object_detonation**
> ObjectDetonation objects_trigger_object_detonation(object, trigger_object_detonation_request)

TriggerObjectDetonation

Triggers a new detonation for the parent object.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.object_detonation import ObjectDetonation
from stairwell_openapi_client.models.trigger_object_detonation_request import TriggerObjectDetonationRequest
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
    api_instance = stairwell_openapi_client.ObjectsApi(api_client)
    object = 'object_example' # str | The object id.
    trigger_object_detonation_request = stairwell_openapi_client.TriggerObjectDetonationRequest() # TriggerObjectDetonationRequest | 

    try:
        # TriggerObjectDetonation
        api_response = await api_instance.objects_trigger_object_detonation(object, trigger_object_detonation_request)
        print("The response of ObjectsApi->objects_trigger_object_detonation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_trigger_object_detonation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| The object id. | 
 **trigger_object_detonation_request** | [**TriggerObjectDetonationRequest**](TriggerObjectDetonationRequest.md)|  | 

### Return type

[**ObjectDetonation**](ObjectDetonation.md)

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

