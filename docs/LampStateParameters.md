# LampStateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brightness** | **float** | the brightness of the light | [optional] 
**master_brightness** | **float** | the master brightness value of the light.  This parameter is new for API schema 4 and provides an independent brightness channel that can be varied while &#x27;Brightness&#x27; remains constant. | [optional] 
**net_brightness** | **float** | The overall brightness of the light (Brightness * MasterBrightness). This parameter is new for API schema 4 and is ignored for a PUT or POST operation. | [optional] 
**dim_curve_active** | **bool** | returns true if a dimming curve is currently active on the lamp group.  New for API schema 4. | [optional] 
**dim_curve** | **str** | if DimCurveActive is true, indicates which dimming curve is active.  New for API schema 4. | [optional] 
**power_on** | **bool** | true if the light is on, false if the light is off | [optional] 
**vibrancy** | **float** | the ratio of RGB to phosphor-converted white LED content.  A value of 0 indicates to use as little RGB as possible.  A value of 1 indicates to use as much RGB as possible | [optional] 
**cct** | **int** | the correlated color temperature of the light.  If cct is provided and within the valid range, it will be used instead of x and y chromaticity | [optional] 
**x_chromaticity** | **float** | the x chromaticity of the light.  This parameter will be ignored if a valid cct value is provided on a put/post operation.  A get operation will return a valid value always | [optional] 
**y_chromaticity** | **float** | the y chromaticity of the light.  This parameter will be ignored if a valid cct value is provided on a put/post operation.  A get operation will return a valid value always | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

