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
    api_instance = aioketraapi.HubOperationsApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

