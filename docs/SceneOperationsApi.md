# aioketraapi.SceneOperationsApi

All URIs are relative to *https://localhost/ketra.cgi/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](SceneOperationsApi.md#root_get) | **GET** / | Get keypads and groups  (and scenes in API schema 4 or later)
[**scenes_get**](SceneOperationsApi.md#scenes_get) | **GET** /Scenes | Get Scenes
[**scenes_scene_id_activate_post**](SceneOperationsApi.md#scenes_scene_id_activate_post) | **POST** /Scenes/{scene-id}/Activate | Activates a scene
[**scenes_scene_id_get**](SceneOperationsApi.md#scenes_scene_id_get) | **GET** /Scenes/{scene-id} | Gets a single scene

# **root_get**
> InlineResponse200 root_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Get keypads and groups  (and scenes in API schema 4 or later)

Gets all keypads and groups in the installation.  Added in hub firmware version 1.14 (API schema 3).   Scenes are also returned in API schema 4.

### Example
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = aioketraapi.SceneOperationsApi(aioketraapi.ApiClient(configuration))
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Get keypads and groups  (and scenes in API schema 4 or later)
    api_response = api_instance.root_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SceneOperationsApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenes_get**
> InlineResponse2005 scenes_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Get Scenes

(New in API schema 4)  Gets the list of defined Scenes.   A scene is a predefined state (or states) for one or more groups of lights.

### Example
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = aioketraapi.SceneOperationsApi(aioketraapi.ApiClient(configuration))
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Get Scenes
    api_response = api_instance.scenes_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SceneOperationsApi->scenes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenes_scene_id_activate_post**
> InlineResponse2007 scenes_scene_id_activate_post(scene_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, group=group, level=level)

Activates a scene

(New in API schema 4)  Activates a Ketra scene specified by {scene-id}.   If a group is specified, the scene will be activated only for that group (and its subgroups).  If no group is specified, the scene will be activated for all groups for which the scene is defined. 

### Example
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = aioketraapi.SceneOperationsApi(aioketraapi.ApiClient(configuration))
scene_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The scene's unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
group = 'group_example' # str | Specifies the parent group for which the scene should be activated (optional)
level = 56 # int | Specifies the master brightness level (from 0 to 65535) at which the scene should be activated.  If this parameter is omitted, the scene will be activated at the maximum level (65535). (optional)

try:
    # Activates a scene
    api_response = api_instance.scenes_scene_id_activate_post(scene_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, group=group, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SceneOperationsApi->scenes_scene_id_activate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | [**str**](.md)| The scene&#x27;s unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **group** | **str**| Specifies the parent group for which the scene should be activated | [optional] 
 **level** | **int**| Specifies the master brightness level (from 0 to 65535) at which the scene should be activated.  If this parameter is omitted, the scene will be activated at the maximum level (65535). | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenes_scene_id_get**
> InlineResponse2006 scenes_scene_id_get(scene_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets a single scene

(New in API schema 4) Gets a Ketra scene specified by {scene-id}. 

### Example
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = aioketraapi.SceneOperationsApi(aioketraapi.ApiClient(configuration))
scene_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The scene's unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Gets a single scene
    api_response = api_instance.scenes_scene_id_get(scene_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SceneOperationsApi->scenes_scene_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | [**str**](.md)| The scene&#x27;s unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

