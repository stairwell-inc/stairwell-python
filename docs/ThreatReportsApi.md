# stairwell_openapi_client.ThreatReportsApi

All URIs are relative to *https://app.stairwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**threat_reports_create_threat_report**](ThreatReportsApi.md#threat_reports_create_threat_report) | **POST** /v1/environments/{environment}/threatReports | CreateThreatReport
[**threat_reports_delete_threat_report**](ThreatReportsApi.md#threat_reports_delete_threat_report) | **DELETE** /v1/environments/{environment}/threatReports/{threatReport} | DeleteThreatReport
[**threat_reports_list_threat_report_iocs**](ThreatReportsApi.md#threat_reports_list_threat_report_iocs) | **GET** /v1/environments/{environment}/threatReports/{threatReport}/iocs | ListThreatReportIocs
[**threat_reports_list_threat_report_matches**](ThreatReportsApi.md#threat_reports_list_threat_report_matches) | **GET** /v1/reportEnvs/{reportEnv}/objEnvs/{objEnv}/threatReports/{threatReport}/matches | ListThreatReportMatches


# **threat_reports_create_threat_report**
> ThreatReport threat_reports_create_threat_report(environment, threat_report)

CreateThreatReport

Upload report will upload a threat report to the Stairwell platform.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.threat_report import ThreatReport
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
    api_instance = stairwell_openapi_client.ThreatReportsApi(api_client)
    environment = 'environment_example' # str | The environment id.
    threat_report = stairwell_openapi_client.ThreatReport() # ThreatReport | 

    try:
        # CreateThreatReport
        api_response = await api_instance.threat_reports_create_threat_report(environment, threat_report)
        print("The response of ThreatReportsApi->threat_reports_create_threat_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatReportsApi->threat_reports_create_threat_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **threat_report** | [**ThreatReport**](ThreatReport.md)|  | 

### Return type

[**ThreatReport**](ThreatReport.md)

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

# **threat_reports_delete_threat_report**
> threat_reports_delete_threat_report(environment, threat_report)

DeleteThreatReport

Delete the report associated with the uid.

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
    api_instance = stairwell_openapi_client.ThreatReportsApi(api_client)
    environment = 'environment_example' # str | The environment id.
    threat_report = 'threat_report_example' # str | The threatReport id.

    try:
        # DeleteThreatReport
        await api_instance.threat_reports_delete_threat_report(environment, threat_report)
    except Exception as e:
        print("Exception when calling ThreatReportsApi->threat_reports_delete_threat_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **threat_report** | **str**| The threatReport id. | 

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

# **threat_reports_list_threat_report_iocs**
> ListThreatReportIocsResponse threat_reports_list_threat_report_iocs(environment, threat_report, page_size=page_size, page_token=page_token)

ListThreatReportIocs

List the threat report IOCs.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_threat_report_iocs_response import ListThreatReportIocsResponse
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
    api_instance = stairwell_openapi_client.ThreatReportsApi(api_client)
    environment = 'environment_example' # str | The environment id.
    threat_report = 'threat_report_example' # str | The threatReport id.
    page_size = 56 # int | The maximum number of IOCs to return. The service may return fewer than this value. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListThreatReportIoc` call. Provide this to retrieve the subsequent page. (optional)

    try:
        # ListThreatReportIocs
        api_response = await api_instance.threat_reports_list_threat_report_iocs(environment, threat_report, page_size=page_size, page_token=page_token)
        print("The response of ThreatReportsApi->threat_reports_list_threat_report_iocs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatReportsApi->threat_reports_list_threat_report_iocs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| The environment id. | 
 **threat_report** | **str**| The threatReport id. | 
 **page_size** | **int**| The maximum number of IOCs to return. The service may return fewer than this value. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListThreatReportIoc&#x60; call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListThreatReportIocsResponse**](ListThreatReportIocsResponse.md)

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

# **threat_reports_list_threat_report_matches**
> ListThreatReportMatchesResponse threat_reports_list_threat_report_matches(report_env, obj_env, threat_report, page_size=page_size, page_token=page_token)

ListThreatReportMatches

List the threat report matches.

### Example

* Api Key Authentication (AuthToken):
```python
import time
import os
import stairwell_openapi_client
from stairwell_openapi_client.models.list_threat_report_matches_response import ListThreatReportMatchesResponse
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
    api_instance = stairwell_openapi_client.ThreatReportsApi(api_client)
    report_env = 'report_env_example' # str | The reportEnv id.
    obj_env = 'obj_env_example' # str | The objEnv id.
    threat_report = 'threat_report_example' # str | The threatReport id.
    page_size = 56 # int | The maximum number of matches to return. The service may return fewer than this value. (optional)
    page_token = 'page_token_example' # str | A page token, received from a previous `ListThreatReportMatches` call. Provide this to retrieve the subsequent page. (optional)

    try:
        # ListThreatReportMatches
        api_response = await api_instance.threat_reports_list_threat_report_matches(report_env, obj_env, threat_report, page_size=page_size, page_token=page_token)
        print("The response of ThreatReportsApi->threat_reports_list_threat_report_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatReportsApi->threat_reports_list_threat_report_matches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_env** | **str**| The reportEnv id. | 
 **obj_env** | **str**| The objEnv id. | 
 **threat_report** | **str**| The threatReport id. | 
 **page_size** | **int**| The maximum number of matches to return. The service may return fewer than this value. | [optional] 
 **page_token** | **str**| A page token, received from a previous &#x60;ListThreatReportMatches&#x60; call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListThreatReportMatchesResponse**](ListThreatReportMatchesResponse.md)

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

