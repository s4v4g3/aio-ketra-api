# LampStateAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transition_time** | **int** | transition time, in ms.  (Required) | [optional] 
**updated_at** | **str** | the time at which the group was last updated.  New for API schema 4. | [optional] 
**transition_complete** | **bool** | returns true if the lamp is finished transitioning to the last updated color.  New for API schema 4. | [optional] 
**active_shows** | **list[int]** | indicates the show groups that are currently active for the group.  New for API schema 4. | [optional] 
**start_state** | [**LampStateParameters**](LampStateParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


