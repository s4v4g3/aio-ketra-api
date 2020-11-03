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
from aioketraapi.models.button import Button  # noqa: E501
from aioketraapi.rest import ApiException

class TestButton(unittest.TestCase):
    """Button unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Button
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aioketraapi.models.button.Button()  # noqa: E501
        if include_optional :
            return Button(
                active = True, 
                id = '0', 
                level = 56, 
                name = '0', 
                position = 56, 
                is_power_button = True, 
                scene_is_modified = True
            )
        else :
            return Button(
        )

    def testButton(self):
        """Test Button"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
