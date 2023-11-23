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
from aioketraapi.models.group import Group  # noqa: E501
from aioketraapi.rest import ApiException


class TestGroup(unittest.TestCase):
    """Group unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Group
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = aioketraapi.models.group.Group()  # noqa: E501
        if include_optional:
            return Group(
                id="0",
                name="0",
                child_groups=["0"],
                parent_groups=["0"],
                address=56,
                state=aioketraapi.models.lamp_state.LampState(),
            )
        else:
            return Group()

    def testGroup(self):
        """Test Group"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
