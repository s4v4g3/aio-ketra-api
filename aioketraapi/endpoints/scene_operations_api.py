# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aioketraapi.api_client import ApiClient


class SceneOperationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def root_get(self, **kwargs):  # noqa: E501
        """Get keypads and groups  (and scenes in API schema 4 or later)  # noqa: E501

        Gets all keypads and groups in the installation.  Added in hub firmware version 1.14 (API schema 3).   Scenes are also returned in API schema 4.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.root_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def root_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get keypads and groups  (and scenes in API schema 4 or later)  # noqa: E501

        Gets all keypads and groups in the installation.  Added in hub firmware version 1.14 (API schema 3).   Scenes are also returned in API schema 4.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['basicauthuser', 'basicauthpassword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method root_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'basicauthuser' in params:
            query_params.append(('basicauthuser', params['basicauthuser']))  # noqa: E501
        if 'basicauthpassword' in params:
            query_params.append(('basicauthpassword', params['basicauthpassword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scenes_get(self, **kwargs):  # noqa: E501
        """Get Scenes  # noqa: E501

        (New in API schema 4)  Gets the list of defined Scenes.   A scene is a predefined state (or states) for one or more groups of lights.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scenes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def scenes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Scenes  # noqa: E501

        (New in API schema 4)  Gets the list of defined Scenes.   A scene is a predefined state (or states) for one or more groups of lights.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['basicauthuser', 'basicauthpassword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'basicauthuser' in params:
            query_params.append(('basicauthuser', params['basicauthuser']))  # noqa: E501
        if 'basicauthpassword' in params:
            query_params.append(('basicauthpassword', params['basicauthpassword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Scenes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scenes_scene_id_activate_post(self, scene_id, **kwargs):  # noqa: E501
        """Activates a scene  # noqa: E501

        (New in API schema 4)  Activates a Ketra scene specified by {scene-id}.   If a group is specified, the scene will be activated only for that group (and its subgroups).  If no group is specified, the scene will be activated for all groups for which the scene is defined.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenes_scene_id_activate_post(scene_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id: The scene's unique identifier (uuid) (required)
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :param str group: Specifies the parent group for which the scene should be activated
        :param int level: Specifies the master brightness level (from 0 to 65535) at which the scene should be activated.  If this parameter is omitted, the scene will be activated at the maximum level (65535).
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenes_scene_id_activate_post_with_http_info(scene_id, **kwargs)  # noqa: E501
        else:
            (data) = self.scenes_scene_id_activate_post_with_http_info(scene_id, **kwargs)  # noqa: E501
            return data

    def scenes_scene_id_activate_post_with_http_info(self, scene_id, **kwargs):  # noqa: E501
        """Activates a scene  # noqa: E501

        (New in API schema 4)  Activates a Ketra scene specified by {scene-id}.   If a group is specified, the scene will be activated only for that group (and its subgroups).  If no group is specified, the scene will be activated for all groups for which the scene is defined.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenes_scene_id_activate_post_with_http_info(scene_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id: The scene's unique identifier (uuid) (required)
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :param str group: Specifies the parent group for which the scene should be activated
        :param int level: Specifies the master brightness level (from 0 to 65535) at which the scene should be activated.  If this parameter is omitted, the scene will be activated at the maximum level (65535).
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scene_id', 'basicauthuser', 'basicauthpassword', 'group', 'level']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenes_scene_id_activate_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scene_id' is set
        if ('scene_id' not in params or
                params['scene_id'] is None):
            raise ValueError("Missing the required parameter `scene_id` when calling `scenes_scene_id_activate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scene_id' in params:
            path_params['scene-id'] = params['scene_id']  # noqa: E501

        query_params = []
        if 'basicauthuser' in params:
            query_params.append(('basicauthuser', params['basicauthuser']))  # noqa: E501
        if 'basicauthpassword' in params:
            query_params.append(('basicauthpassword', params['basicauthpassword']))  # noqa: E501
        if 'group' in params:
            query_params.append(('group', params['group']))  # noqa: E501
        if 'level' in params:
            query_params.append(('level', params['level']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Scenes/{scene-id}/Activate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scenes_scene_id_get(self, scene_id, **kwargs):  # noqa: E501
        """Gets a single scene  # noqa: E501

        (New in API schema 4) Gets a Ketra scene specified by {scene-id}.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenes_scene_id_get(scene_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id: The scene's unique identifier (uuid) (required)
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenes_scene_id_get_with_http_info(scene_id, **kwargs)  # noqa: E501
        else:
            (data) = self.scenes_scene_id_get_with_http_info(scene_id, **kwargs)  # noqa: E501
            return data

    def scenes_scene_id_get_with_http_info(self, scene_id, **kwargs):  # noqa: E501
        """Gets a single scene  # noqa: E501

        (New in API schema 4) Gets a Ketra scene specified by {scene-id}.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenes_scene_id_get_with_http_info(scene_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id: The scene's unique identifier (uuid) (required)
        :param str basicauthuser: Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request.
        :param str basicauthpassword: Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scene_id', 'basicauthuser', 'basicauthpassword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenes_scene_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scene_id' is set
        if ('scene_id' not in params or
                params['scene_id'] is None):
            raise ValueError("Missing the required parameter `scene_id` when calling `scenes_scene_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scene_id' in params:
            path_params['scene-id'] = params['scene_id']  # noqa: E501

        query_params = []
        if 'basicauthuser' in params:
            query_params.append(('basicauthuser', params['basicauthuser']))  # noqa: E501
        if 'basicauthpassword' in params:
            query_params.append(('basicauthpassword', params['basicauthpassword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Scenes/{scene-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
