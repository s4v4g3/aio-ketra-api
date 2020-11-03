# aioketraapi.HubOperationsApi

All URIs are relative to *https://localhost/ketra.cgi/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hub_get**](HubOperationsApi.md#hub_get) | **GET** /Hub | Gets properties of the hub

# **hub_get**
> InlineResponse2004 hub_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets properties of the hub

Gets informational and diagnostic properties of the hub.  Added in hub firmware version 1.14 (API schema 3).

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
api_instance = aioketraapi.HubOperationsApi(aioketraapi.ApiClient(configuration))
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Gets properties of the hub
    api_response = api_instance.hub_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubOperationsApi->hub_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

