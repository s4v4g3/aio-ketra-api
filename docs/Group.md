# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the group | [optional] 
**name** | **str** | Name of the group | [optional] 
**child_groups** | **list[str]** | Ids of child groups of this group.  Added in API Schema 4 (firmware version 1.15).  For this to be populated, the hub must be published with Design Studio 2.0 and the SupportsZoneKeypads property returned in GET /Hub must be true.  See the API overview document for more explanation. | [optional] 
**parent_groups** | **list[str]** | Ids of parent groups of this group.  Added in API Schema 4 (firmware version 1.15).  For this to be populated, the hub must be published with Design Studio 2.0 and the SupportsZoneKeypads property returned in GET /Hub must be true.  See the API overview document for more explanation. | [optional] 
**address** | **int** | The logical address of the group.  Added in API Schema 4 (firmware version 1.15) | [optional] 
**state** | [**LampState**](LampState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

