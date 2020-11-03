from aioketraapi.models.group import Group as GroupModel
from aioketraapi.models.lamp_state import LampState as LampStateModel
from aioketraapi.endpoints.group_operations_api import GroupOperationsApi
from aioketraapi.model_helper import model_to_json



class Group(GroupModel):
    def __init__(self, group_model: GroupModel, hub):
        super().__init__(**group_model.to_dict())
        self.hub = hub


    def update_from_model(self, group_model: GroupModel):
        for k,v in group_model.to_dict().items():
            setattr(self, k, v)

    async def update_state(self):
        async with self.hub.api_client() as api_client:
            updated_group = await GroupOperationsApi(api_client).groups_group_id_state_get(self.id)
            self.update_from_model(updated_group.content)

    async def set_state(self, lamp_state: LampStateModel, **kwargs):
        async with self.hub.api_client() as api_client:
            lamp_state_json = model_to_json(lamp_state)
            for attr in list(lamp_state_json.keys()):
                if lamp_state_json[attr] is None:
                    lamp_state_json.pop(attr)
            updated_group = await GroupOperationsApi(api_client).groups_group_id_state_put(lamp_state_json, self.id, **kwargs)
            self.update_from_model(updated_group.content)





