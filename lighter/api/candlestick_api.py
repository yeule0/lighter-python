# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from lighter.models.candlesticks import Candlesticks
from lighter.models.fundings import Fundings

from lighter.api_client import ApiClient, RequestSerialized
from lighter.api_response import ApiResponse
from lighter.rest import RESTResponseType


class CandlestickApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def candlesticks(
        self,
        market_id: StrictInt,
        resolution: StrictStr,
        start_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        end_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        count_back: StrictInt,
        set_timestamp_to_end: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Candlesticks:
        """candlesticks

        Get candlesticks

        :param market_id: (required)
        :type market_id: int
        :param resolution: (required)
        :type resolution: str
        :param start_timestamp: (required)
        :type start_timestamp: int
        :param end_timestamp: (required)
        :type end_timestamp: int
        :param count_back: (required)
        :type count_back: int
        :param set_timestamp_to_end:
        :type set_timestamp_to_end: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._candlesticks_serialize(
            market_id=market_id,
            resolution=resolution,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            count_back=count_back,
            set_timestamp_to_end=set_timestamp_to_end,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Candlesticks",
            '400': "ResultCode",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def candlesticks_with_http_info(
        self,
        market_id: StrictInt,
        resolution: StrictStr,
        start_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        end_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        count_back: StrictInt,
        set_timestamp_to_end: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Candlesticks]:
        """candlesticks

        Get candlesticks

        :param market_id: (required)
        :type market_id: int
        :param resolution: (required)
        :type resolution: str
        :param start_timestamp: (required)
        :type start_timestamp: int
        :param end_timestamp: (required)
        :type end_timestamp: int
        :param count_back: (required)
        :type count_back: int
        :param set_timestamp_to_end:
        :type set_timestamp_to_end: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._candlesticks_serialize(
            market_id=market_id,
            resolution=resolution,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            count_back=count_back,
            set_timestamp_to_end=set_timestamp_to_end,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Candlesticks",
            '400': "ResultCode",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def candlesticks_without_preload_content(
        self,
        market_id: StrictInt,
        resolution: StrictStr,
        start_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        end_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        count_back: StrictInt,
        set_timestamp_to_end: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """candlesticks

        Get candlesticks

        :param market_id: (required)
        :type market_id: int
        :param resolution: (required)
        :type resolution: str
        :param start_timestamp: (required)
        :type start_timestamp: int
        :param end_timestamp: (required)
        :type end_timestamp: int
        :param count_back: (required)
        :type count_back: int
        :param set_timestamp_to_end:
        :type set_timestamp_to_end: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._candlesticks_serialize(
            market_id=market_id,
            resolution=resolution,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            count_back=count_back,
            set_timestamp_to_end=set_timestamp_to_end,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Candlesticks",
            '400': "ResultCode",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _candlesticks_serialize(
        self,
        market_id,
        resolution,
        start_timestamp,
        end_timestamp,
        count_back,
        set_timestamp_to_end,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if market_id is not None:
            
            _query_params.append(('market_id', market_id))
            
        if resolution is not None:
            
            _query_params.append(('resolution', resolution))
            
        if start_timestamp is not None:
            
            _query_params.append(('start_timestamp', start_timestamp))
            
        if end_timestamp is not None:
            
            _query_params.append(('end_timestamp', end_timestamp))
            
        if count_back is not None:
            
            _query_params.append(('count_back', count_back))
            
        if set_timestamp_to_end is not None:
            
            _query_params.append(('set_timestamp_to_end', set_timestamp_to_end))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/candlesticks',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def fundings(
        self,
        market_id: StrictInt,
        resolution: StrictStr,
        start_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        end_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        count_back: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Fundings:
        """fundings

        Get fundings

        :param market_id: (required)
        :type market_id: int
        :param resolution: (required)
        :type resolution: str
        :param start_timestamp: (required)
        :type start_timestamp: int
        :param end_timestamp: (required)
        :type end_timestamp: int
        :param count_back: (required)
        :type count_back: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._fundings_serialize(
            market_id=market_id,
            resolution=resolution,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            count_back=count_back,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Fundings",
            '400': "ResultCode",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def fundings_with_http_info(
        self,
        market_id: StrictInt,
        resolution: StrictStr,
        start_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        end_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        count_back: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Fundings]:
        """fundings

        Get fundings

        :param market_id: (required)
        :type market_id: int
        :param resolution: (required)
        :type resolution: str
        :param start_timestamp: (required)
        :type start_timestamp: int
        :param end_timestamp: (required)
        :type end_timestamp: int
        :param count_back: (required)
        :type count_back: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._fundings_serialize(
            market_id=market_id,
            resolution=resolution,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            count_back=count_back,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Fundings",
            '400': "ResultCode",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def fundings_without_preload_content(
        self,
        market_id: StrictInt,
        resolution: StrictStr,
        start_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        end_timestamp: Annotated[int, Field(le=5000000000000, strict=True, ge=0)],
        count_back: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """fundings

        Get fundings

        :param market_id: (required)
        :type market_id: int
        :param resolution: (required)
        :type resolution: str
        :param start_timestamp: (required)
        :type start_timestamp: int
        :param end_timestamp: (required)
        :type end_timestamp: int
        :param count_back: (required)
        :type count_back: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._fundings_serialize(
            market_id=market_id,
            resolution=resolution,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            count_back=count_back,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Fundings",
            '400': "ResultCode",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _fundings_serialize(
        self,
        market_id,
        resolution,
        start_timestamp,
        end_timestamp,
        count_back,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if market_id is not None:
            
            _query_params.append(('market_id', market_id))
            
        if resolution is not None:
            
            _query_params.append(('resolution', resolution))
            
        if start_timestamp is not None:
            
            _query_params.append(('start_timestamp', start_timestamp))
            
        if end_timestamp is not None:
            
            _query_params.append(('end_timestamp', end_timestamp))
            
        if count_back is not None:
            
            _query_params.append(('count_back', count_back))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/fundings',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


