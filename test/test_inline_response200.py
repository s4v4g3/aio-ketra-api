# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aioketraapi
from aioketraapi.models.inline_response200 import InlineResponse200  # noqa: E501
from aioketraapi.rest import ApiException


class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = aioketraapi.models.inline_response200.InlineResponse200()  # noqa: E501
        if include_optional:
            return InlineResponse200(
                success=True,
                error="0",
                content=aioketraapi.models.inline_response_200_content.inline_response_200_Content(
                    keypads=[
                        aioketraapi.models.keypad.Keypad(
                            id="0",
                            is_virtual=True,
                            level=56,
                            name="0",
                            serial_number="0",
                            buttons=[
                                aioketraapi.models.button.Button(
                                    active=True,
                                    id="0",
                                    level=56,
                                    name="0",
                                    position=56,
                                    is_power_button=True,
                                    scene_is_modified=True,
                                )
                            ],
                        )
                    ],
                    groups=[
                        aioketraapi.models.group.Group(
                            id="0",
                            name="0",
                            child_groups=["0"],
                            parent_groups=["0"],
                            address=56,
                            state=aioketraapi.models.lamp_state.LampState(),
                        )
                    ],
                    scenes=[
                        aioketraapi.models.scene.Scene(
                            id="0",
                            content_id=56,
                            is_show=True,
                            show_group_number=56,
                            name="0",
                            parent_group_ids=["0"],
                        )
                    ],
                ),
            )
        else:
            return InlineResponse200()

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
