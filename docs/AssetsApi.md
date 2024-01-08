# stairwell_openapi_client.AssetsApi

All URIs are relative to *https://app.stairwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_create_tag**](AssetsApi.md#assets_create_tag) | **POST** /v1/assets/{asset}/tags | CreateTag
[**assets_delete_tag**](AssetsApi.md#assets_delete_tag) | **DELETE** /v1/assets/{asset}/tags/{tag} | DeleteTag
[**assets_get_asset**](AssetsApi.md#assets_get_asset) | **GET** /v1/assets/{asset} | GetAsset
[**assets_get_tag**](AssetsApi.md#assets_get_tag) | **GET** /v1/assets/{asset}/tags/{tag} | GetTag
[**assets_list_assets**](AssetsApi.md#assets_list_assets) | **GET** /v1/environments/{environment}/assets | ListAssets
[**assets_list_tags**](AssetsApi.md#assets_list_tags) | **GET** /v1/assets/{asset}/tags | ListTags


# **assets_create_tag**
> Tag assets_create_tag(asset, tag)

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
    api_instance = stairwell_openapi_client.AssetsApi(api_client)
    asset = 'asset_example' # str | The asset id.
    tag = stairwell_openapi_client.Tag() # Tag | 

    try:
        # CreateTag
        api_response = await api_instance.assets_create_tag(asset, tag)
        print("The response of AssetsApi->assets_create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_create_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The asset id. | 
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

# **assets_delete_tag**
> assets_delete_tag(asset, tag)

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
    api_instance = stairwell_openapi_client.AssetsApi(api_client)
    asset = 'asset_example' # str | The asset id.
    tag = 'tag_example' # str | The tag id.

    try:
        # DeleteTag
        await api_instance.assets_delete_tag(asset, tag)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The asset id. | 
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

# **assets_get_asset**
> Asset assets_get_asset(asset)

GetAsset

Gets metadata for a particular asset.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.asset import Asset
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
    api_instance = stairwell_openapi_client.AssetsApi(api_client)
    asset = 'asset_example' # str | The asset id.

    try:
        # GetAsset
        api_response = await api_instance.assets_get_asset(asset)
        print("The response of AssetsApi->assets_get_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The asset id. | 

### Return type

[**Asset**](Asset.md)

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

# **assets_get_tag**
> Tag assets_get_tag(asset, tag)

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
    api_instance = stairwell_openapi_client.AssetsApi(api_client)
    asset = 'asset_example' # str | The asset id.
    tag = 'tag_example' # str | The tag id.

    try:
        # GetTag
        api_response = await api_instance.assets_get_tag(asset, tag)
        print("The response of AssetsApi->assets_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The asset id. | 
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

# **assets_list_assets**
> ListAssetsResponse assets_list_assets(environment, page_size=page_size, page_token=page_token)

ListAssets

Lists the assets in an environment.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_assets_response import ListAssetsResponse
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
    api_instance = stairwell_openapi_client.AssetsApi(api_client)
    environment = 'environment_example' # str | The environment id.
    page_size = 56 # int | The number of assets to return in a single page (optional)
    page_token = 'page_token_example' # str | The page token for getting successive pages (optional)

    try:
        # ListAssets
        api_response = await api_instance.assets_list_assets(environment, page_size=page_size, page_token=page_token)
        print("The response of AssetsApi->assets_list_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_list_assets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **page_size** | **int**| The number of assets to return in a single page | [optional] 
 **page_token** | **str**| The page token for getting successive pages | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

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

# **assets_list_tags**
> ListTagsResponse assets_list_tags(asset, page_size=page_size, page_token=page_token)

ListTags

Gets the tags for the specified asset.

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
    api_instance = stairwell_openapi_client.AssetsApi(api_client)
    asset = 'asset_example' # str | The asset id.
    page_size = 56 # int | The maximum number of tags to return. The service may return fewer than this value. If unspecified, at most 100 tags will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListTags` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTags` must match the call that provided the page token. (optional)

    try:
        # ListTags
        api_response = await api_instance.assets_list_tags(asset, page_size=page_size, page_token=page_token)
        print("The response of AssetsApi->assets_list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_list_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The asset id. | 
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

