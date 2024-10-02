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

from stairwell_openapi_client.models.list_trigger_matches_response import ListTriggerMatchesResponse

from stairwell_openapi_client.api_client import ApiClient
from stairwell_openapi_client.api_response import ApiResponse
from stairwell_openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TriggersServiceApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    async def triggers_service_list_trigger_matches(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], filter_newest_time_seconds : Annotated[Optional[StrictInt], Field(description="Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.")] = None, filter_newest_time_nanos : Annotated[Optional[StrictInt], Field(description="Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.")] = None, filter_oldest_time_seconds : Annotated[Optional[StrictInt], Field(description="Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.")] = None, filter_oldest_time_nanos : Annotated[Optional[StrictInt], Field(description="Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.")] = None, page_size : Annotated[Optional[StrictInt], Field(description="The number of trigger matches to return in a single page.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="The page token for getting successive pages")] = None, **kwargs) -> ListTriggerMatchesResponse:  # noqa: E501
        """ListTriggerMatches  # noqa: E501

        Lists ListTriggerMatches  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param filter_newest_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :type filter_newest_time_seconds: int
        :param filter_newest_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.
        :type filter_newest_time_nanos: int
        :param filter_oldest_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :type filter_oldest_time_seconds: int
        :param filter_oldest_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.
        :type filter_oldest_time_nanos: int
        :param page_size: The number of trigger matches to return in a single page.
        :type page_size: int
        :param page_token: The page token for getting successive pages
        :type page_token: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListTriggerMatchesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the triggers_service_list_trigger_matches_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.triggers_service_list_trigger_matches_with_http_info(environment, filter_newest_time_seconds, filter_newest_time_nanos, filter_oldest_time_seconds, filter_oldest_time_nanos, page_size, page_token, **kwargs)  # noqa: E501

    @validate_arguments
    async def triggers_service_list_trigger_matches_with_http_info(self, environment : Annotated[StrictStr, Field(..., description="The environment id.")], filter_newest_time_seconds : Annotated[Optional[StrictInt], Field(description="Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.")] = None, filter_newest_time_nanos : Annotated[Optional[StrictInt], Field(description="Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.")] = None, filter_oldest_time_seconds : Annotated[Optional[StrictInt], Field(description="Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.")] = None, filter_oldest_time_nanos : Annotated[Optional[StrictInt], Field(description="Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.")] = None, page_size : Annotated[Optional[StrictInt], Field(description="The number of trigger matches to return in a single page.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="The page token for getting successive pages")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """ListTriggerMatches  # noqa: E501

        Lists ListTriggerMatches  # noqa: E501

        :param environment: The environment id. (required)
        :type environment: str
        :param filter_newest_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :type filter_newest_time_seconds: int
        :param filter_newest_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.
        :type filter_newest_time_nanos: int
        :param filter_oldest_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :type filter_oldest_time_seconds: int
        :param filter_oldest_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive.
        :type filter_oldest_time_nanos: int
        :param page_size: The number of trigger matches to return in a single page.
        :type page_size: int
        :param page_token: The page token for getting successive pages
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
        :rtype: tuple(ListTriggerMatchesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'environment',
            'filter_newest_time_seconds',
            'filter_newest_time_nanos',
            'filter_oldest_time_seconds',
            'filter_oldest_time_nanos',
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
                    " to method triggers_service_list_trigger_matches" % _key
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
        if _params.get('filter_newest_time_seconds') is not None:  # noqa: E501
            _query_params.append(('filter.newestTime.seconds', _params['filter_newest_time_seconds']))

        if _params.get('filter_newest_time_nanos') is not None:  # noqa: E501
            _query_params.append(('filter.newestTime.nanos', _params['filter_newest_time_nanos']))

        if _params.get('filter_oldest_time_seconds') is not None:  # noqa: E501
            _query_params.append(('filter.oldestTime.seconds', _params['filter_oldest_time_seconds']))

        if _params.get('filter_oldest_time_nanos') is not None:  # noqa: E501
            _query_params.append(('filter.oldestTime.nanos', _params['filter_oldest_time_nanos']))

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
            '200': "ListTriggerMatchesResponse",
        }

        return await self.api_client.call_api(
            '/v1/environments/{environment}/triggerMatches', 'GET',
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
