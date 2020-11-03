# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2004(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'success': 'bool',
        'error': 'str',
        'content': 'InlineResponse2004Content'
    }

    attribute_map = {
        'success': 'Success',
        'error': 'Error',
        'content': 'Content'
    }

    def __init__(self, success=None, error=None, content=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._error = None
        self._content = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if error is not None:
            self.error = error
        if content is not None:
            self.content = content

    @property
    def success(self):
        """Gets the success of this InlineResponse2004.  # noqa: E501

        true if the transaction was successful, false if an error occurred  # noqa: E501

        :return: The success of this InlineResponse2004.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse2004.

        true if the transaction was successful, false if an error occurred  # noqa: E501

        :param success: The success of this InlineResponse2004.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def error(self):
        """Gets the error of this InlineResponse2004.  # noqa: E501

        error message  # noqa: E501

        :return: The error of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse2004.

        error message  # noqa: E501

        :param error: The error of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def content(self):
        """Gets the content of this InlineResponse2004.  # noqa: E501


        :return: The content of this InlineResponse2004.  # noqa: E501
        :rtype: InlineResponse2004Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse2004.


        :param content: The content of this InlineResponse2004.  # noqa: E501
        :type: InlineResponse2004Content
        """

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2004, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
