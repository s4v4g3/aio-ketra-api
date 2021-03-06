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
from aioketraapi.models.inline_response2007 import InlineResponse2007  # noqa: E501
from aioketraapi.rest import ApiException

class TestInlineResponse2007(unittest.TestCase):
    """InlineResponse2007 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2007
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aioketraapi.models.inline_response2007.InlineResponse2007()  # noqa: E501
        if include_optional :
            return InlineResponse2007(
                success = True, 
                error = '0', 
                content = None
            )
        else :
            return InlineResponse2007(
        )

    def testInlineResponse2007(self):
        """Test InlineResponse2007"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
