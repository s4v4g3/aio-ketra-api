# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import aioketraapi
from aioketraapi.api.lamp_operations_api import LampOperationsApi  # noqa: E501
from aioketraapi.rest import ApiException


class TestLampOperationsApi(unittest.TestCase):
    """LampOperationsApi unit test stubs"""

    def setUp(self):
        self.api = aioketraapi.api.lamp_operations_api.LampOperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lamps_get(self):
        """Test case for lamps_get

        Gets lamps in the installation  # noqa: E501
        """
        pass

    def test_lamps_lamp_id_get(self):
        """Test case for lamps_lamp_id_get

        Gets a lamp by its id  # noqa: E501
        """
        pass

    def test_lamps_lamp_id_state_put(self):
        """Test case for lamps_lamp_id_state_put

        sets a lamp state  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
