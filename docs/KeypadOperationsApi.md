# aioketraapi.KeypadOperationsApi

All URIs are relative to *https://localhost/ketra.cgi/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_button_post**](KeypadOperationsApi.md#activate_button_post) | **POST** /ActivateButton | Activate a button
[**deactivate_button_post**](KeypadOperationsApi.md#deactivate_button_post) | **POST** /DeactivateButton | Deactivate a button
[**keypads_get**](KeypadOperationsApi.md#keypads_get) | **GET** /Keypads | Get keypads
[**keypads_keypad_id_buttons_button_id_activate_post**](KeypadOperationsApi.md#keypads_keypad_id_buttons_button_id_activate_post) | **POST** /Keypads/{keypad-id}/Buttons/{button-id}/Activate | Activate a button
[**keypads_keypad_id_buttons_button_id_deactivate_post**](KeypadOperationsApi.md#keypads_keypad_id_buttons_button_id_deactivate_post) | **POST** /Keypads/{keypad-id}/Buttons/{button-id}/Deactivate | Deactivate a button
[**keypads_keypad_id_buttons_button_id_get**](KeypadOperationsApi.md#keypads_keypad_id_buttons_button_id_get) | **GET** /Keypads/{keypad-id}/Buttons/{button-id} | Gets the specified button for a specified keypad
[**keypads_keypad_id_buttons_button_id_push_button_post**](KeypadOperationsApi.md#keypads_keypad_id_buttons_button_id_push_button_post) | **POST** /Keypads/{keypad-id}/Buttons/{button-id}/PushButton | Pushes a button
[**keypads_keypad_id_buttons_get**](KeypadOperationsApi.md#keypads_keypad_id_buttons_get) | **GET** /Keypads/{keypad-id}/Buttons | Gets the buttons for a keypad
[**keypads_keypad_id_get**](KeypadOperationsApi.md#keypads_keypad_id_get) | **GET** /Keypads/{keypad-id} | Gets a single keypad
[**keypads_keypad_id_set_level_post**](KeypadOperationsApi.md#keypads_keypad_id_set_level_post) | **POST** /Keypads/{keypad-id}/SetLevel | sets the master intensity level for a single keypad
[**push_button_post**](KeypadOperationsApi.md#push_button_post) | **POST** /PushButton | Deactivate a button
[**root_get**](KeypadOperationsApi.md#root_get) | **GET** / | Get keypads and groups  (and scenes in API schema 4 or later)

# **activate_button_post**
> InlineResponse2009 activate_button_post(body, keypad_name, button_name, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Activate a button

Activates the scene or show represented by the button 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
body = aioketraapi.Level() # Level | The level
keypad_name = 'keypad_name_example' # str | Specifies a keypad name
button_name = 'button_name_example' # str | Specifies a button name
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Activate a button
    api_response = api_instance.activate_button_post(body, keypad_name, button_name, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->activate_button_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Level**](Level.md)| The level | 
 **keypad_name** | **str**| Specifies a keypad name | 
 **button_name** | **str**| Specifies a button name | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_button_post**
> InlineResponse2009 deactivate_button_post(body, keypad_name, button_name, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Deactivate a button

Deactivates the scene or show represented by the button 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
body = aioketraapi.Level() # Level | The level
keypad_name = 'keypad_name_example' # str | Specifies a keypad name
button_name = 'button_name_example' # str | Specifies a button name
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Deactivate a button
    api_response = api_instance.deactivate_button_post(body, keypad_name, button_name, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->deactivate_button_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Level**](Level.md)| The level | 
 **keypad_name** | **str**| Specifies a keypad name | 
 **button_name** | **str**| Specifies a button name | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_get**
> InlineResponse2008 keypads_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name, includeall=includeall, nobuttons=nobuttons)

Get keypads

Gets the list of Ketra keypads.  By default, unless the includeall parameter is provided and set to true, cascaded and mirrored keypads are not returned in the list. However, the buttons of cascaded keypads are returned with their respective master keypad. 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
name = 'name_example' # str | If specified, returns only the keypads matching the name provided (optional)
includeall = false # bool | if true, cascaded and mirrored keypads will be returned in the list.  If false or the parameter is not provided, cascaded keypad buttons will be returned as children of their master keypad. (optional) (default to false)
nobuttons = false # bool | if true, the buttons array will not be populated and only the keypad objects will be returned.  For an installation with a large number of keypads this can be much quicker than returning the full set of keypads along with all buttons. (optional) (default to false)

try:
    # Get keypads
    api_response = api_instance.keypads_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name, includeall=includeall, nobuttons=nobuttons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **name** | **str**| If specified, returns only the keypads matching the name provided | [optional] 
 **includeall** | **bool**| if true, cascaded and mirrored keypads will be returned in the list.  If false or the parameter is not provided, cascaded keypad buttons will be returned as children of their master keypad. | [optional] [default to false]
 **nobuttons** | **bool**| if true, the buttons array will not be populated and only the keypad objects will be returned.  For an installation with a large number of keypads this can be much quicker than returning the full set of keypads along with all buttons. | [optional] [default to false]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_buttons_button_id_activate_post**
> InlineResponse2009 keypads_keypad_id_buttons_button_id_activate_post(body, keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Activate a button

Activates the scene or show represented by the button 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
body = aioketraapi.Level() # Level | The level
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
button_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The button's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Activate a button
    api_response = api_instance.keypads_keypad_id_buttons_button_id_activate_post(body, keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_buttons_button_id_activate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Level**](Level.md)| The level | 
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **button_id** | [**str**](.md)| The button&#x27;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_buttons_button_id_deactivate_post**
> InlineResponse2009 keypads_keypad_id_buttons_button_id_deactivate_post(body, keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Deactivate a button

Deactivates the scene or show represented by the button 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
body = aioketraapi.Level() # Level | The level
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
button_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The button's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Deactivate a button
    api_response = api_instance.keypads_keypad_id_buttons_button_id_deactivate_post(body, keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_buttons_button_id_deactivate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Level**](Level.md)| The level | 
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **button_id** | [**str**](.md)| The button&#x27;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_buttons_button_id_get**
> InlineResponse20011 keypads_keypad_id_buttons_button_id_get(keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets the specified button for a specified keypad

Gets the button specified by {button-id} for the keypad specified by {keypad-id}. 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
button_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The button's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Gets the specified button for a specified keypad
    api_response = api_instance.keypads_keypad_id_buttons_button_id_get(keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_buttons_button_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **button_id** | [**str**](.md)| The button&#x27;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_buttons_button_id_push_button_post**
> InlineResponse2009 keypads_keypad_id_buttons_button_id_push_button_post(keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, idempotency_key=idempotency_key)

Pushes a button

Performs the same action as a physical press of the button.  The action performed is determined by the current state of the button and the type of keypad.   Added in hub firmware version 1.12 (API schema 2). 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
button_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The button's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
idempotency_key = 'idempotency_key_example' # str | optional string to guarantee this action will execute only once on the server.  Set this to a random string  and future requests with the same string will be ignored (optional)

try:
    # Pushes a button
    api_response = api_instance.keypads_keypad_id_buttons_button_id_push_button_post(keypad_id, button_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_buttons_button_id_push_button_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **button_id** | [**str**](.md)| The button&#x27;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **idempotency_key** | **str**| optional string to guarantee this action will execute only once on the server.  Set this to a random string  and future requests with the same string will be ignored | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_buttons_get**
> InlineResponse20010 keypads_keypad_id_buttons_get(keypad_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name)

Gets the buttons for a keypad

Gets the buttons for the keypad specified by {keypad-id}.  If a keypad name is specified instead of a uuid, the buttons for the first keypad matching the specified name will be returned 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
name = 'name_example' # str | If specified, returns only the buttons matching the name provided (optional)

try:
    # Gets the buttons for a keypad
    api_response = api_instance.keypads_keypad_id_buttons_get(keypad_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_buttons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **name** | **str**| If specified, returns only the buttons matching the name provided | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_get**
> InlineResponse2009 keypads_keypad_id_get(keypad_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

Gets a single keypad

Gets a Ketra keypad speficied by {keypad-id}.  If a keypad name is specified instead of a uuid, the first keypad matching the specified name will be returned 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Gets a single keypad
    api_response = api_instance.keypads_keypad_id_get(keypad_id, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keypads_keypad_id_set_level_post**
> InlineResponse2009 keypads_keypad_id_set_level_post(keypad_id, level, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)

sets the master intensity level for a single keypad

Sets the keypad's intensity (brightness) slider to the level specified by the level parameter

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
keypad_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The keypad's name or unique identifier (uuid)
level = true # bool | The level
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # sets the master intensity level for a single keypad
    api_response = api_instance.keypads_keypad_id_set_level_post(keypad_id, level, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->keypads_keypad_id_set_level_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_id** | [**str**](.md)| The keypad&#x27;s name or unique identifier (uuid) | 
 **level** | **bool**| The level | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_button_post**
> InlineResponse2009 push_button_post(keypad_name, button_name, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, idempotency_key=idempotency_key)

Deactivate a button

Performs the same action as a physical press of the button.  The action performed is determined by the current state of the button and the type of keypad. 

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
keypad_name = 'keypad_name_example' # str | Specifies a keypad name
button_name = 'button_name_example' # str | Specifies a button name
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)
idempotency_key = 'idempotency_key_example' # str | optional string to guarantee this action will execute only once on the server.  Set this to a random string  and future requests with the same string will be ignored (optional)

try:
    # Deactivate a button
    api_response = api_instance.push_button_post(keypad_name, button_name, basicauthuser=basicauthuser, basicauthpassword=basicauthpassword, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->push_button_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_name** | **str**| Specifies a keypad name | 
 **button_name** | **str**| Specifies a button name | 
 **basicauthuser** | **str**| Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. | [optional] 
 **basicauthpassword** | **str**| Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. | [optional] 
 **idempotency_key** | **str**| optional string to guarantee this action will execute only once on the server.  Set this to a random string  and future requests with the same string will be ignored | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = aioketraapi.KeypadOperationsApi(aioketraapi.ApiClient(configuration))
basicauthuser = 'basicauthuser_example' # str | Username to use in place of username in basic authentication header.  For a secure installation, this value is ignored but still must be supplied unless a basic authentication header is sent with the request. (optional)
basicauthpassword = 'basicauthpassword_example' # str | Password to use in place of password in basic authentication header. For a secure installation, this should be an oauth token for a user with access to the installation.  If a basic authentication header is sent, this parameter is ignored.  If no basic authentication header is sent, this parameter as well as the basicauthuser parameter must be supplied if the hub is a member of a secure installation. (optional)

try:
    # Get keypads and groups  (and scenes in API schema 4 or later)
    api_response = api_instance.root_get(basicauthuser=basicauthuser, basicauthpassword=basicauthpassword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeypadOperationsApi->root_get: %s\n" % e)
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

