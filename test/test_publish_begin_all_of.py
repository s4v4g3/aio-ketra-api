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
from aioketraapi.models.publish_begin_all_of import PublishBeginAllOf  # noqa: E501
from aioketraapi.rest import ApiException


class TestPublishBeginAllOf(unittest.TestCase):
    """PublishBeginAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PublishBeginAllOf
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = aioketraapi.models.publish_begin_all_of.PublishBeginAllOf()  # noqa: E501
        if include_optional:
            return PublishBeginAllOf(
                notification_type="ButtonChange",
                time_utc=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
            )
        else:
            return PublishBeginAllOf(
                notification_type="ButtonChange",
                time_utc=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
            )

    def testPublishBeginAllOf(self):
        """Test PublishBeginAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
