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
from aioketraapi.api.keypad_operations_api import KeypadOperationsApi  # noqa: E501
from aioketraapi.rest import ApiException


class TestKeypadOperationsApi(unittest.TestCase):
    """KeypadOperationsApi unit test stubs"""

    def setUp(self):
        self.api = (
            aioketraapi.api.keypad_operations_api.KeypadOperationsApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_button_post(self):
        """Test case for activate_button_post

        Activate a button  # noqa: E501
        """
        pass

    def test_deactivate_button_post(self):
        """Test case for deactivate_button_post

        Deactivate a button  # noqa: E501
        """
        pass

    def test_keypads_get(self):
        """Test case for keypads_get

        Get keypads  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_buttons_button_id_activate_post(self):
        """Test case for keypads_keypad_id_buttons_button_id_activate_post

        Activate a button  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_buttons_button_id_deactivate_post(self):
        """Test case for keypads_keypad_id_buttons_button_id_deactivate_post

        Deactivate a button  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_buttons_button_id_get(self):
        """Test case for keypads_keypad_id_buttons_button_id_get

        Gets the specified button for a specified keypad  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_buttons_button_id_push_button_post(self):
        """Test case for keypads_keypad_id_buttons_button_id_push_button_post

        Pushes a button  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_buttons_get(self):
        """Test case for keypads_keypad_id_buttons_get

        Gets the buttons for a keypad  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_get(self):
        """Test case for keypads_keypad_id_get

        Gets a single keypad  # noqa: E501
        """
        pass

    def test_keypads_keypad_id_set_level_post(self):
        """Test case for keypads_keypad_id_set_level_post

        sets the master intensity level for a single keypad  # noqa: E501
        """
        pass

    def test_push_button_post(self):
        """Test case for push_button_post

        Deactivate a button  # noqa: E501
        """
        pass

    def test_root_get(self):
        """Test case for root_get

        Get keypads and groups  (and scenes in API schema 4 or later)  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
