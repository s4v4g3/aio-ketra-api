# InlineResponse2004Content

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_schema** | **int** | API schema version supported by the hub&#39;s firmware | [optional] 
**cpu_version** | **str** | the version of the hub&#39;s CPU firmware | [optional] 
**radio_version** | **str** | the version of the hub&#39;s radio firmware | [optional] 
**serial_number** | **str** | the hub&#39;s serial number | [optional] 
**model_name** | **str** | the model name of the hub | [optional] 
**id** | **str** | the unique identifier of the hub | [optional] 
**installation_id** | **str** | the unique identifier of the hub&#39;s installation | [optional] 
**installation_name** | **str** | the name of the hub&#39;s installation | [optional] 
**network_id** | **str** | the unique identifier of the hub&#39;s network | [optional] 
**name** | **str** | the user-assigned name of the hub | [optional] 
**ethernet_mac** | **str** | the hub&#39;s ethernet MAC address | [optional] 
**i_pv4_address** | **str** | the hub&#39;s IPv4 address | [optional] 
**ethernet_link_status** | **list[bool]** | the link status of the hub&#39;s ethernet ports. This is an array of length equal to the number of ethernet ports on the hub.  Each element will be true or false depending on whether a link was detected on the port or not. | [optional] 
**up_time_seconds** | **int** | the number of seconds since last power cycle or reboot | [optional] 
**local_time** | **str** | the local time | [optional] 
**utc_time** | **str** | the time in UTC | [optional] 
**last_reboot_reason** | **str** | the reason for the last reboot | [optional] 
**has_internet_connectivity** | **bool** | does the hub have internet access? | [optional] 
**last_time_update_was_successful** | **bool** | was the last time update successful? | [optional] 
**remote_connection_enabled** | **bool** | is remote connectivity enabled? | [optional] 
**remote_connection_established** | **bool** | is the remote connection established? | [optional] 
**supports_zone_keypads** | **bool** | This property will be true if the hub was published in Design Studio 2.0 in an installation containing devices that all have 1.15 firmware.  This signifies that a keypad&#39;s buttons can be configured to control independent zones and are not restricted to controlling the same set of groups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


