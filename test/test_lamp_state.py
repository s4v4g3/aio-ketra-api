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
from aioketraapi.models.lamp_state import LampState  # noqa: E501
from aioketraapi.rest import ApiException

class TestLampState(unittest.TestCase):
    """LampState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LampState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aioketraapi.models.lamp_state.LampState()  # noqa: E501
        if include_optional :
            return LampState(
                brightness = 0, 
                master_brightness = 0, 
                net_brightness = 0, 
                dim_curve_active = True, 
                dim_curve = 'Xenon', 
                power_on = True, 
                vibrancy = 0, 
                cct = 0, 
                x_chromaticity = 0, 
                y_chromaticity = 0, 
                transition_time = 0, 
                updated_at = '0', 
                transition_complete = True, 
                active_shows = [
                    56
                    ], 
                start_state = aioketraapi.models.lamp_state_parameters.LampStateParameters(
                    brightness = 0, 
                    master_brightness = 0, 
                    net_brightness = 0, 
                    dim_curve_active = True, 
                    dim_curve = 'Xenon', 
                    power_on = True, 
                    vibrancy = 0, 
                    cct = 0, 
                    x_chromaticity = 0, 
                    y_chromaticity = 0, )
            )
        else :
            return LampState(
        )

    def testLampState(self):
        """Test LampState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
