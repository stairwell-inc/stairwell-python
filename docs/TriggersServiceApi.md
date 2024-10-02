# stairwell_openapi_client.TriggersServiceApi

All URIs are relative to *https://app.stairwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggers_service_list_trigger_matches**](TriggersServiceApi.md#triggers_service_list_trigger_matches) | **GET** /v1/environments/{environment}/triggerMatches | ListTriggerMatches


# **triggers_service_list_trigger_matches**
> ListTriggerMatchesResponse triggers_service_list_trigger_matches(environment, filter_newest_time_seconds=filter_newest_time_seconds, filter_newest_time_nanos=filter_newest_time_nanos, filter_oldest_time_seconds=filter_oldest_time_seconds, filter_oldest_time_nanos=filter_oldest_time_nanos, page_size=page_size, page_token=page_token)

ListTriggerMatches

Lists ListTriggerMatches

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_trigger_matches_response import ListTriggerMatchesResponse
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
    api_instance = stairwell_openapi_client.TriggersServiceApi(api_client)
    environment = 'environment_example' # str | The environment id.
    filter_newest_time_seconds = 56 # int | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
    filter_newest_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. (optional)
    filter_oldest_time_seconds = 56 # int | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
    filter_oldest_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. (optional)
    page_size = 56 # int | The number of trigger matches to return in a single page. (optional)
    page_token = 'page_token_example' # str | The page token for getting successive pages (optional)

    try:
        # ListTriggerMatches
        api_response = await api_instance.triggers_service_list_trigger_matches(environment, filter_newest_time_seconds=filter_newest_time_seconds, filter_newest_time_nanos=filter_newest_time_nanos, filter_oldest_time_seconds=filter_oldest_time_seconds, filter_oldest_time_nanos=filter_oldest_time_nanos, page_size=page_size, page_token=page_token)
        print("The response of TriggersServiceApi->triggers_service_list_trigger_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersServiceApi->triggers_service_list_trigger_matches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **filter_newest_time_seconds** | **int**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **filter_newest_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. | [optional] 
 **filter_oldest_time_seconds** | **int**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **filter_oldest_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. | [optional] 
 **page_size** | **int**| The number of trigger matches to return in a single page. | [optional] 
 **page_token** | **str**| The page token for getting successive pages | [optional] 

### Return type

[**ListTriggerMatchesResponse**](ListTriggerMatchesResponse.md)

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

