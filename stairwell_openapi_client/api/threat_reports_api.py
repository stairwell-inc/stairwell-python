# coding: utf-8

"""
    Stairwell V1 HTTP APIs

    Restful APIs for the Stairwell platform. Most APIs expose named resources: each resource has a unique identifier that users use to reference that resource, and these names are what users should store as the canonical names for the resources. The base URL for this API is https://app.stairwell.com

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from stairwell_openapi_client.models.list_threat_report_iocs_response import ListThreatReportIocsResponse
from stairwell_openapi_client.models.list_threat_report_matches_response import ListThreatReportMatchesResponse
from stairwell_openapi_client.models.threat_report import ThreatReport

from stairwell_openapi_client.api_client import ApiClient
from stairwell_openapi_client.api_response import ApiResponse
from stairwell_openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ThreatReportsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    async def threat_reports_create_threat_report(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], threat_report : ThreatReport, **kwargs) -> ThreatReport:  # noqa: E501
        """CreateThreatReport  # noqa: E501

        Upload report will upload a threat report to the Stairwell platform.  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param threat_report: (required)
        :type threat_report: ThreatReport
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ThreatReport
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the threat_reports_create_threat_report_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.threat_reports_create_threat_report_with_http_info(environment, threat_report, **kwargs)  # noqa: E501

    @validate_arguments
    async def threat_reports_create_threat_report_with_http_info(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], threat_report : ThreatReport, **kwargs) -> ApiResponse:  # noqa: E501
        """CreateThreatReport  # noqa: E501

        Upload report will upload a threat report to the Stairwell platform.  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param threat_report: (required)
        :type threat_report: ThreatReport
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ThreatReport, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'environment',
            'threat_report'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method threat_reports_create_threat_report" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['environment'] is not None:
            _path_params['environment'] = _params['environment']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['threat_report'] is not None:
            _body_params = _params['threat_report']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AuthToken']  # noqa: E501

        _response_types_map = {
            '200': "ThreatReport",
        }

        return await self.api_client.call_api(
            '/v1/environments/{environment}/threatReports', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def threat_reports_delete_threat_report(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], threat_report : Annotated[StrictStr, Field(..., description="The threatReport id.")], **kwargs) -> None:  # noqa: E501
        """DeleteThreatReport  # noqa: E501

        Delete the report associated with the uid.  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param threat_report: The threatReport id. (required)
        :type threat_report: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the threat_reports_delete_threat_report_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.threat_reports_delete_threat_report_with_http_info(environment, threat_report, **kwargs)  # noqa: E501

    @validate_arguments
    async def threat_reports_delete_threat_report_with_http_info(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], threat_report : Annotated[StrictStr, Field(..., description="The threatReport id.")], **kwargs) -> ApiResponse:  # noqa: E501
        """DeleteThreatReport  # noqa: E501

        Delete the report associated with the uid.  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param threat_report: The threatReport id. (required)
        :type threat_report: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'environment',
            'threat_report'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method threat_reports_delete_threat_report" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['environment'] is not None:
            _path_params['environment'] = _params['environment']

        if _params['threat_report'] is not None:
            _path_params['threatReport'] = _params['threat_report']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['AuthToken']  # noqa: E501

        _response_types_map = {}

        return await self.api_client.call_api(
            '/v1/environments/{environment}/threatReports/{threatReport}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def threat_reports_list_threat_report_iocs(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], threat_report : Annotated[StrictStr, Field(..., description="The threatReport id.")], page_size : Annotated[Optional[StrictInt], Field(description="The maximum number of IOCs to return. The service may return fewer than this value.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A page token, received from a previous `ListThreatReportIoc` call. Provide this to retrieve the subsequent page.")] = None, **kwargs) -> ListThreatReportIocsResponse:  # noqa: E501
        """ListThreatReportIocs  # noqa: E501

        List the threat report IOCs.  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param threat_report: The threatReport id. (required)
        :type threat_report: str
        :param page_size: The maximum number of IOCs to return. The service may return fewer than this value.
        :type page_size: int
        :param page_token: A page token, received from a previous `ListThreatReportIoc` call. Provide this to retrieve the subsequent page.
        :type page_token: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListThreatReportIocsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the threat_reports_list_threat_report_iocs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.threat_reports_list_threat_report_iocs_with_http_info(environment, threat_report, page_size, page_token, **kwargs)  # noqa: E501

    @validate_arguments
    async def threat_reports_list_threat_report_iocs_with_http_info(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], threat_report : Annotated[StrictStr, Field(..., description="The threatReport id.")], page_size : Annotated[Optional[StrictInt], Field(description="The maximum number of IOCs to return. The service may return fewer than this value.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A page token, received from a previous `ListThreatReportIoc` call. Provide this to retrieve the subsequent page.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """ListThreatReportIocs  # noqa: E501

        List the threat report IOCs.  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param threat_report: The threatReport id. (required)
        :type threat_report: str
        :param page_size: The maximum number of IOCs to return. The service may return fewer than this value.
        :type page_size: int
        :param page_token: A page token, received from a previous `ListThreatReportIoc` call. Provide this to retrieve the subsequent page.
        :type page_token: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListThreatReportIocsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'environment',
            'threat_report',
            'page_size',
            'page_token'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method threat_reports_list_threat_report_iocs" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['environment'] is not None:
            _path_params['environment'] = _params['environment']

        if _params['threat_report'] is not None:
            _path_params['threatReport'] = _params['threat_report']


        # process the query parameters
        _query_params = []
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        if _params.get('page_token') is not None:  # noqa: E501
            _query_params.append(('pageToken', _params['page_token']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AuthToken']  # noqa: E501

        _response_types_map = {
            '200': "ListThreatReportIocsResponse",
        }

        return await self.api_client.call_api(
            '/v1/environments/{environment}/threatReports/{threatReport}/iocs', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def threat_reports_list_threat_report_matches(self, report_env : Annotated[StrictStr, Field(..., description="The reportEnv id.")], obj_env : Annotated[StrictStr, Field(..., description="The objEnv id.")], threat_report : Annotated[StrictStr, Field(..., description="The threatReport id.")], page_size : Annotated[Optional[StrictInt], Field(description="The maximum number of matches to return. The service may return fewer than this value.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A page token, received from a previous `ListThreatReportMatches` call. Provide this to retrieve the subsequent page.")] = None, **kwargs) -> ListThreatReportMatchesResponse:  # noqa: E501
        """ListThreatReportMatches  # noqa: E501

        List the threat report matches.  # noqa: E501

        :param report_env: The reportEnv id. (required)
        :type report_env: str
        :param obj_env: The objEnv id. (required)
        :type obj_env: str
        :param threat_report: The threatReport id. (required)
        :type threat_report: str
        :param page_size: The maximum number of matches to return. The service may return fewer than this value.
        :type page_size: int
        :param page_token: A page token, received from a previous `ListThreatReportMatches` call. Provide this to retrieve the subsequent page.
        :type page_token: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListThreatReportMatchesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the threat_reports_list_threat_report_matches_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.threat_reports_list_threat_report_matches_with_http_info(report_env, obj_env, threat_report, page_size, page_token, **kwargs)  # noqa: E501

    @validate_arguments
    async def threat_reports_list_threat_report_matches_with_http_info(self, report_env : Annotated[StrictStr, Field(..., description="The reportEnv id.")], obj_env : Annotated[StrictStr, Field(..., description="The objEnv id.")], threat_report : Annotated[StrictStr, Field(..., description="The threatReport id.")], page_size : Annotated[Optional[StrictInt], Field(description="The maximum number of matches to return. The service may return fewer than this value.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A page token, received from a previous `ListThreatReportMatches` call. Provide this to retrieve the subsequent page.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """ListThreatReportMatches  # noqa: E501

        List the threat report matches.  # noqa: E501

        :param report_env: The reportEnv id. (required)
        :type report_env: str
        :param obj_env: The objEnv id. (required)
        :type obj_env: str
        :param threat_report: The threatReport id. (required)
        :type threat_report: str
        :param page_size: The maximum number of matches to return. The service may return fewer than this value.
        :type page_size: int
        :param page_token: A page token, received from a previous `ListThreatReportMatches` call. Provide this to retrieve the subsequent page.
        :type page_token: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListThreatReportMatchesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'report_env',
            'obj_env',
            'threat_report',
            'page_size',
            'page_token'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method threat_reports_list_threat_report_matches" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['report_env'] is not None:
            _path_params['reportEnv'] = _params['report_env']

        if _params['obj_env'] is not None:
            _path_params['objEnv'] = _params['obj_env']

        if _params['threat_report'] is not None:
            _path_params['threatReport'] = _params['threat_report']


        # process the query parameters
        _query_params = []
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        if _params.get('page_token') is not None:  # noqa: E501
            _query_params.append(('pageToken', _params['page_token']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AuthToken']  # noqa: E501

        _response_types_map = {
            '200': "ListThreatReportMatchesResponse",
        }

        return await self.api_client.call_api(
            '/v1/reportEnvs/{reportEnv}/objEnvs/{objEnv}/threatReports/{threatReport}/matches', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
