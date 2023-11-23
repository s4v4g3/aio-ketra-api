import aiohttp
import logging
from typing import Dict, Optional

_LOGGER = logging.getLogger(__name__)


async def get_installations(oauth_token: str) -> Optional[Dict[str, str]]:
    """
    Returns a dict of installation_id -> installation_title for the given oauth_token

    :param oauth_token:      authentication token for user account
    :return:                 dict of installation_id -> installation_title
    """
    async with aiohttp.ClientSession() as client:
        async with client.get(
            f"https://my.goketra.com/api/v4/locations.json?access_token={oauth_token}"
        ) as response:
            if response.status != 200:
                _LOGGER.warning(
                    "Received status code %s when querying for accessible installations",
                    str(response.status),
                )
                return None
            api_resp = await response.json()
        installations = api_resp["content"]
        async with client.get("https://my.goketra.com/api/n4/v1/query") as response:
            if response.status != 200:
                _LOGGER.warning(
                    "Received status code %s when querying for hubs",
                    str(response.status),
                )
                return None
            api_resp = await response.json()
            local_installation_ids = [
                inst["installation_id"] for inst in api_resp["content"]
            ]
            return {
                inst["id"]: inst["title"]
                for inst in installations
                if inst["id"] in local_installation_ids
            }
