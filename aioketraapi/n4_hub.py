import aiohttp
from asyncio import AbstractEventLoop
from aioketraapi import KeypadOperationsApi
from aioketraapi import GroupOperationsApi
from aioketraapi import ApiClient
from aioketraapi import Configuration
from aioketraapi.keypad import Keypad
from aioketraapi.group import Group
from aioketraapi import WebsocketV2Notification
import json





class N4Hub():
    def __init__(self, url_base :str, oauth_token :str, loop :AbstractEventLoop=None):
        self.url_base = url_base
        ws_url_tmp, _, _ = url_base.rpartition('/')
        self.ws_url = f"{ws_url_tmp.replace('https', 'wss')}/notifications"
        self.oauth_token = oauth_token
        self.is_local = "api.goketra.com" not in url_base
        self.client_config = Configuration()
        self.client_config.host = f"{self.url_base}/api/v1"
        self.client_config.username = "na"
        self.client_config.password = self.oauth_token
        self.client_config.loop = loop
        if self.is_local:
            self.client_config.verify_ssl = False
        self.connected_websocket = None


    @classmethod
    async def get_hub(cls, installation_id, oauth_token, use_cloud = False, loop=None):
        query_url = f"https://my.goketra.com/api/n4/v1/query?installation_id={installation_id}"
        async with aiohttp.ClientSession(loop=loop) as session:
            async with session.get(query_url) as response:
                if response.status == 200:
                    hub_query_resp = await response.json()
                    if hub_query_resp['success'] == 'true' and len(hub_query_resp['content']) > 0:
                        first_hub = hub_query_resp['content'][0]
                        if use_cloud:
                            url = f"https://api.goketra.com/{installation_id}/{first_hub['serial_number']}/webAPI"
                            return N4Hub(url, oauth_token)
                        else:
                            url = f"https://{first_hub['internal_ip']}/ketra.cgi"
                            return N4Hub(url, oauth_token, loop)
            return None

    def api_client(self):
        return ApiClient(configuration=self.client_config)

    async def get_keypads(self, **kwargs):
        async with self.api_client() as api_client:
            kp_api = KeypadOperationsApi(api_client)
            response_model = await kp_api.keypads_get(**kwargs)
            return [Keypad(keypad, self) for keypad in response_model.content]

    async def get_groups(self, include_internal=False, **kwargs):
        async with self.api_client() as api_client:
            kp_api = GroupOperationsApi(api_client)
            response_model = await kp_api.groups_get(**kwargs)
            return [Group(group, self) for group in response_model.content if include_internal or 'Internal_MasterGroup' not in group.name]

    async def connect_websocket(self, notify_callback):
        async with self.api_client() as api_client:
            async with api_client.rest_client.client_session.ws_connect(self.ws_url) as ws:
                # from https://s3.amazonaws.com/ketra-software/KetraMobileAPI/v1/KetraN4WebsocketProtocol.pdf
                msg = [0x06, 0x00, 0x0F]
                msg.append((len(self.oauth_token) >> 8) & 0xFF)
                msg.append(len(self.oauth_token) & 0xFF)
                msg.extend([b for b in self.oauth_token.encode('ascii')])
                await ws.send_bytes(bytearray(msg))
                self.connected_websocket = ws
                async for recv_msg in ws:
                    if recv_msg.type == aiohttp.WSMsgType.TEXT:
                        model = api_client.deserialize(recv_msg, WebsocketV2Notification)
                        notify_callback(model)
                    elif recv_msg.type == aiohttp.WSMsgType.BINARY:
                        # ignore this message
                        pass
                    else: # CLOSING, CLOSED, etc.
                        self.connected_websocket = None
                        break

    async def disconnect_websocket(self):
        if self.connected_websocket is not None:
            await self.connected_websocket.close()
            self.connected_websocket = None









