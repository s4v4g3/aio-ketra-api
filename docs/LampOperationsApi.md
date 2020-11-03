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
api_instance = aioketraapi.LampOperationsApi(aioketraapi.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lamps_lamp_id_get**
> InlineResponse2002 lamps_lamp_id_get(lamp_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets a lamp by its id

placeholder

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
api_instance = aioketraapi.LampOperationsApi(aioketraapi.ApiClient(configuration))
lamp_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The lamp's unique identifier (uuid)
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
 **lamp_id** | [**str**](.md)| The lamp&#x27;s unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lamps_lamp_id_state_put**
> InlineResponse2003 lamps_lamp_id_state_put(body, lamp_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

sets a lamp state

sets a lamp state

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
api_instance = aioketraapi.LampOperationsApi(aioketraapi.ApiClient(configuration))
body = aioketraapi.LampState() # LampState | Color settings to apply to the lamp
lamp_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The lamp's unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # sets a lamp state
    api_response = api_instance.lamps_lamp_id_state_put(body, lamp_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LampOperationsApi->lamps_lamp_id_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LampState**](LampState.md)| Color settings to apply to the lamp | 
 **lamp_id** | [**str**](.md)| The lamp&#x27;s unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

