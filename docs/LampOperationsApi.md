# aioketraapi.LampOperationsApi

All URIs are relative to *https://localhost/ketra.cgi/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lamps_get**](LampOperationsApi.md#lamps_get) | **GET** /lamps | Gets lamps in the installation
[**lamps_lamp_id_get**](LampOperationsApi.md#lamps_lamp_id_get) | **GET** /lamps/{lamp-id} | Gets a lamp by its id
[**lamps_lamp_id_state_put**](LampOperationsApi.md#lamps_lamp_id_state_put) | **PUT** /lamps/{lamp-id}/state | sets a lamp state


# **lamps_get**
> InlineResponse2001 lamps_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets lamps in the installation

placeholder

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
    api_instance = aioketraapi.LampOperationsApi(api_client)
    basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # Gets lamps in the installation
        api_response = api_instance.lamps_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LampOperationsApi->lamps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | good |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lamps_lamp_id_get**
> InlineResponse2002 lamps_lamp_id_get(lamp_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets a lamp by its id

placeholder

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
    api_instance = aioketraapi.LampOperationsApi(api_client)
    lamp_id = 'lamp_id_example' # str | The lamp's unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # Gets a lamp by its id
        api_response = api_instance.lamps_lamp_id_get(lamp_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LampOperationsApi->lamps_lamp_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lamp_id** | [**str**](.md)| The lamp&#39;s unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | good |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lamps_lamp_id_state_put**
> InlineResponse2003 lamps_lamp_id_state_put(lamp_id, lamp_state, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

sets a lamp state

sets a lamp state

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
    api_instance = aioketraapi.LampOperationsApi(api_client)
    lamp_id = 'lamp_id_example' # str | The lamp's unique identifier (uuid)
lamp_state = aioketraapi.LampState() # LampState | Color settings to apply to the lamp
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

    try:
        # sets a lamp state
        api_response = api_instance.lamps_lamp_id_state_put(lamp_id, lamp_state, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LampOperationsApi->lamps_lamp_id_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lamp_id** | [**str**](.md)| The lamp&#39;s unique identifier (uuid) | 
 **lamp_state** | [**LampState**](LampState.md)| Color settings to apply to the lamp | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | good |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

