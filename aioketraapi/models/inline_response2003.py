# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aioketraapi.configuration import Configuration


class InlineResponse2003(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'success': 'bool',
        'error': 'str'
    }

    attribute_map = {
        'success': 'Success',
        'error': 'Error'
    }

    def __init__(self, success=None, error=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2003 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._error = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if error is not None:
            self.error = error

    @property
    def success(self):
        """Gets the success of this InlineResponse2003.  # noqa: E501

        true if the transaction was successful, false if an error occurred  # noqa: E501

        :return: The success of this InlineResponse2003.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse2003.

        true if the transaction was successful, false if an error occurred  # noqa: E501

        :param success: The success of this InlineResponse2003.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def error(self):
        """Gets the error of this InlineResponse2003.  # noqa: E501

        error message  # noqa: E501

        :return: The error of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse2003.

        error message  # noqa: E501

        :param error: The error of this InlineResponse2003.  # noqa: E501
        :type error: str
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2003):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2003):
            return True

        return self.to_dict() != other.to_dict()
