# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aioketraapi.api_client import ApiClient
from aioketraapi.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class LampOperationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lamps_get(self, **kwargs):  # noqa: E501
        """Gets lamps in the installation  # noqa: E501

        placeholder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lamps_get(async_req=True)
        >>> result = thread.get()

        :param basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :type basicauthuser: str
        :param basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :type basicauthpassword: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2001
        """
        kwargs["_return_http_data_only"] = True
        return self.lamps_get_with_http_info(**kwargs)  # noqa: E501

    def lamps_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets lamps in the installation  # noqa: E501

        placeholder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lamps_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :type basicauthuser: str
        :param basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :type basicauthpassword: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse2001, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["basicauthuser", "basicauthpassword"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lamps_get" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if (
            "basicauthuser" in local_var_params
            and local_var_params["basicauthuser"] is not None
        ):  # noqa: E501
            query_params.append(
                ("basicauthuser", local_var_params["basicauthuser"])
            )  # noqa: E501
        if (
            "basicauthpassword" in local_var_params
            and local_var_params["basicauthpassword"] is not None
        ):  # noqa: E501
            query_params.append(
                ("basicauthpassword", local_var_params["basicauthpassword"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/lamps",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2001",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def lamps_lamp_id_get(self, lamp_id, **kwargs):  # noqa: E501
        """Gets a lamp by its id  # noqa: E501

        placeholder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lamps_lamp_id_get(lamp_id, async_req=True)
        >>> result = thread.get()

        :param lamp_id: The lamp's unique identifier (uuid) (required)
        :type lamp_id: str
        :param basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :type basicauthuser: str
        :param basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :type basicauthpassword: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2002
        """
        kwargs["_return_http_data_only"] = True
        return self.lamps_lamp_id_get_with_http_info(lamp_id, **kwargs)  # noqa: E501

    def lamps_lamp_id_get_with_http_info(self, lamp_id, **kwargs):  # noqa: E501
        """Gets a lamp by its id  # noqa: E501

        placeholder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lamps_lamp_id_get_with_http_info(lamp_id, async_req=True)
        >>> result = thread.get()

        :param lamp_id: The lamp's unique identifier (uuid) (required)
        :type lamp_id: str
        :param basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :type basicauthuser: str
        :param basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :type basicauthpassword: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse2002, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["lamp_id", "basicauthuser", "basicauthpassword"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lamps_lamp_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'lamp_id' is set
        if self.api_client.client_side_validation and (
            "lamp_id" not in local_var_params
            or local_var_params["lamp_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `lamp_id` when calling `lamps_lamp_id_get`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "lamp_id" in local_var_params:
            path_params["lamp-id"] = local_var_params["lamp_id"]  # noqa: E501

        query_params = []
        if (
            "basicauthuser" in local_var_params
            and local_var_params["basicauthuser"] is not None
        ):  # noqa: E501
            query_params.append(
                ("basicauthuser", local_var_params["basicauthuser"])
            )  # noqa: E501
        if (
            "basicauthpassword" in local_var_params
            and local_var_params["basicauthpassword"] is not None
        ):  # noqa: E501
            query_params.append(
                ("basicauthpassword", local_var_params["basicauthpassword"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/lamps/{lamp-id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2002",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def lamps_lamp_id_state_put(self, lamp_id, lamp_state, **kwargs):  # noqa: E501
        """sets a lamp state  # noqa: E501

        sets a lamp state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lamps_lamp_id_state_put(lamp_id, lamp_state, async_req=True)
        >>> result = thread.get()

        :param lamp_id: The lamp's unique identifier (uuid) (required)
        :type lamp_id: str
        :param lamp_state: Color settings to apply to the lamp (required)
        :type lamp_state: LampState
        :param basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :type basicauthuser: str
        :param basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :type basicauthpassword: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2003
        """
        kwargs["_return_http_data_only"] = True
        return self.lamps_lamp_id_state_put_with_http_info(
            lamp_id, lamp_state, **kwargs
        )  # noqa: E501

    def lamps_lamp_id_state_put_with_http_info(
        self, lamp_id, lamp_state, **kwargs
    ):  # noqa: E501
        """sets a lamp state  # noqa: E501

        sets a lamp state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lamps_lamp_id_state_put_with_http_info(lamp_id, lamp_state, async_req=True)
        >>> result = thread.get()

        :param lamp_id: The lamp's unique identifier (uuid) (required)
        :type lamp_id: str
        :param lamp_state: Color settings to apply to the lamp (required)
        :type lamp_state: LampState
        :param basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :type basicauthuser: str
        :param basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :type basicauthpassword: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse2003, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["lamp_id", "lamp_state", "basicauthuser", "basicauthpassword"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lamps_lamp_id_state_put" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'lamp_id' is set
        if self.api_client.client_side_validation and (
            "lamp_id" not in local_var_params
            or local_var_params["lamp_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `lamp_id` when calling `lamps_lamp_id_state_put`"
            )  # noqa: E501
        # verify the required parameter 'lamp_state' is set
        if self.api_client.client_side_validation and (
            "lamp_state" not in local_var_params
            or local_var_params["lamp_state"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `lamp_state` when calling `lamps_lamp_id_state_put`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "lamp_id" in local_var_params:
            path_params["lamp-id"] = local_var_params["lamp_id"]  # noqa: E501

        query_params = []
        if (
            "basicauthuser" in local_var_params
            and local_var_params["basicauthuser"] is not None
        ):  # noqa: E501
            query_params.append(
                ("basicauthuser", local_var_params["basicauthuser"])
            )  # noqa: E501
        if (
            "basicauthpassword" in local_var_params
            and local_var_params["basicauthpassword"] is not None
        ):  # noqa: E501
            query_params.append(
                ("basicauthpassword", local_var_params["basicauthpassword"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "lamp_state" in local_var_params:
            body_params = local_var_params["lamp_state"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/lamps/{lamp-id}/state",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2003",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
