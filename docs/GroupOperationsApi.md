# aioketraapi.GroupOperationsApi

All URIs are relative to *https://localhost/ketra.cgi/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get**](GroupOperationsApi.md#groups_get) | **GET** /Groups | Gets the list of groups
[**groups_group_id_get**](GroupOperationsApi.md#groups_group_id_get) | **GET** /Groups/{group-id} | Gets a single group object
[**groups_group_id_state_get**](GroupOperationsApi.md#groups_group_id_state_get) | **GET** /Groups/{group-id}/State | Gets the state of a single lamp group
[**groups_group_id_state_put**](GroupOperationsApi.md#groups_group_id_state_put) | **PUT** /Groups/{group-id}/State | Sets the state of a single lamp group
[**groups_state_post**](GroupOperationsApi.md#groups_state_post) | **POST** /Groups/State | Sets the state of a lamp group
[**root_get**](GroupOperationsApi.md#root_get) | **GET** / | Get keypads and groups  (and scenes in API schema 4 or later)


# **groups_get**
> InlineResponse20012 groups_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name)

Gets the list of groups

Gets the list of lamp groups in the system 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/ketra.cgi/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioketraapi.Configuration(
    host = "https://localhost/ketra.cgi/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with aioketraapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioketraapi.GroupOperationsApi(api_client)
    basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
name = 'name_example' # str | If specified, only the groups matching the string provided are returned (optional)

    try:
        # Gets the list of groups
        api_response = api_instance.groups_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupOperationsApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **name** | **str**| If specified, only the groups matching the string provided are returned | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_get**
> InlineResponse20013 groups_group_id_get(group_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets a single group object

Gets the group specified by {group-id}.  If a group name is specified instead of a uuid, the first group matching the specified name will be returned

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/ketra.cgi/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioketraapi.Configuration(
    host = "https://localhost/ketra.cgi/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with aioketraapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioketraapi.GroupOperationsApi(api_client)
    group_id = 'group_id_example' # str | The group's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # Gets a single group object
        api_response = api_instance.groups_group_id_get(group_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupOperationsApi->groups_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| The group&#39;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_state_get**
> InlineResponse20014 groups_group_id_state_get(group_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets the state of a single lamp group

Gets the state of the group specified by {group-id}.   If a group name is specified instead of a uuid, the state of the first group matching the specified name will be returned.  Note that for API schema 3 (hub firmware 1.14) or earlier, this will only reflect the state of the last group operation -- light changes due to keypad operations are not reflected in the returned state.  However in API schema 4 / hub firmware 1.15, if the hub is published with Design Studio 2.0 (and the 'SupportsZoneKeypads' property returned in GET /Hub is true), the lamp state returned will reflect the current state of the group.  Please see the API overview document for more discussion on this topic.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/ketra.cgi/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioketraapi.Configuration(
    host = "https://localhost/ketra.cgi/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with aioketraapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioketraapi.GroupOperationsApi(api_client)
    group_id = 'group_id_example' # str | The group's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # Gets the state of a single lamp group
        api_response = api_instance.groups_group_id_state_get(group_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupOperationsApi->groups_group_id_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| The group&#39;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_state_put**
> InlineResponse20014 groups_group_id_state_put(group_id, lamp_state, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Sets the state of a single lamp group

Set the state of the group specified by {group-id}.  If a group name is specified instead of a uuid, the state of the first group matching the specified name will be set

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/ketra.cgi/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioketraapi.Configuration(
    host = "https://localhost/ketra.cgi/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with aioketraapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioketraapi.GroupOperationsApi(api_client)
    group_id = 'group_id_example' # str | The group's name or unique identifier (uuid)
lamp_state = aioketraapi.LampState() # LampState | Color settings to apply to the lamp group
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # Sets the state of a single lamp group
        api_response = api_instance.groups_group_id_state_put(group_id, lamp_state, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupOperationsApi->groups_group_id_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| The group&#39;s name or unique identifier (uuid) | 
 **lamp_state** | [**LampState**](LampState.md)| Color settings to apply to the lamp group | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_state_post**
> InlineResponse20014 groups_state_post(lamp_state, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name)

Sets the state of a lamp group

Sets the state of a lamp group specified by a name query parameters

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/ketra.cgi/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioketraapi.Configuration(
    host = "https://localhost/ketra.cgi/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with aioketraapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioketraapi.GroupOperationsApi(api_client)
    lamp_state = aioketraapi.LampState() # LampState | Color settings to apply to the lamp group
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
name = 'name_example' # str | name of the group to apply the state (optional)

    try:
        # Sets the state of a lamp group
        api_response = api_instance.groups_state_post(lamp_state, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupOperationsApi->groups_state_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lamp_state** | [**LampState**](LampState.md)| Color settings to apply to the lamp group | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **name** | **str**| name of the group to apply the state | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> InlineResponse200 root_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Get keypads and groups  (and scenes in API schema 4 or later)

Gets all keypads and groups in the installation.  Added in hub firmware version 1.14 (API schema 3).   Scenes are also returned in API schema 4.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import aioketraapi
from aioketraapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/ketra.cgi/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aioketraapi.Configuration(
    host = "https://localhost/ketra.cgi/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aioketraapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with aioketraapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aioketraapi.GroupOperationsApi(api_client)
    basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # Get keypads and groups  (and scenes in API schema 4 or later)
        api_response = api_instance.root_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupOperationsApi->root_get: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | No user credentials specified. |  -  |
**403** | Invalid user credentials specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

