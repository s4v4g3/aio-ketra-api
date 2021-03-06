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


class LampStateAllOf(object):
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
        'transition_time': 'int',
        'updated_at': 'str',
        'transition_complete': 'bool',
        'active_shows': 'list[int]',
        'start_state': 'LampStateParameters'
    }

    attribute_map = {
        'transition_time': 'TransitionTime',
        'updated_at': 'UpdatedAt',
        'transition_complete': 'TransitionComplete',
        'active_shows': 'ActiveShows',
        'start_state': 'StartState'
    }

    def __init__(self, transition_time=None, updated_at=None, transition_complete=None, active_shows=None, start_state=None, local_vars_configuration=None):  # noqa: E501
        """LampStateAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transition_time = None
        self._updated_at = None
        self._transition_complete = None
        self._active_shows = None
        self._start_state = None
        self.discriminator = None

        if transition_time is not None:
            self.transition_time = transition_time
        if updated_at is not None:
            self.updated_at = updated_at
        if transition_complete is not None:
            self.transition_complete = transition_complete
        if active_shows is not None:
            self.active_shows = active_shows
        if start_state is not None:
            self.start_state = start_state

    @property
    def transition_time(self):
        """Gets the transition_time of this LampStateAllOf.  # noqa: E501

        transition time, in ms.  (Required)  # noqa: E501

        :return: The transition_time of this LampStateAllOf.  # noqa: E501
        :rtype: int
        """
        return self._transition_time

    @transition_time.setter
    def transition_time(self, transition_time):
        """Sets the transition_time of this LampStateAllOf.

        transition time, in ms.  (Required)  # noqa: E501

        :param transition_time: The transition_time of this LampStateAllOf.  # noqa: E501
        :type transition_time: int
        """
        if (self.local_vars_configuration.client_side_validation and
                transition_time is not None and transition_time > 6553500):  # noqa: E501
            raise ValueError("Invalid value for `transition_time`, must be a value less than or equal to `6553500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transition_time is not None and transition_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `transition_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transition_time = transition_time

    @property
    def updated_at(self):
        """Gets the updated_at of this LampStateAllOf.  # noqa: E501

        the time at which the group was last updated.  New for API schema 4.  # noqa: E501

        :return: The updated_at of this LampStateAllOf.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LampStateAllOf.

        the time at which the group was last updated.  New for API schema 4.  # noqa: E501

        :param updated_at: The updated_at of this LampStateAllOf.  # noqa: E501
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def transition_complete(self):
        """Gets the transition_complete of this LampStateAllOf.  # noqa: E501

        returns true if the lamp is finished transitioning to the last updated color.  New for API schema 4.  # noqa: E501

        :return: The transition_complete of this LampStateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._transition_complete

    @transition_complete.setter
    def transition_complete(self, transition_complete):
        """Sets the transition_complete of this LampStateAllOf.

        returns true if the lamp is finished transitioning to the last updated color.  New for API schema 4.  # noqa: E501

        :param transition_complete: The transition_complete of this LampStateAllOf.  # noqa: E501
        :type transition_complete: bool
        """

        self._transition_complete = transition_complete

    @property
    def active_shows(self):
        """Gets the active_shows of this LampStateAllOf.  # noqa: E501

        indicates the show groups that are currently active for the group.  New for API schema 4.  # noqa: E501

        :return: The active_shows of this LampStateAllOf.  # noqa: E501
        :rtype: list[int]
        """
        return self._active_shows

    @active_shows.setter
    def active_shows(self, active_shows):
        """Sets the active_shows of this LampStateAllOf.

        indicates the show groups that are currently active for the group.  New for API schema 4.  # noqa: E501

        :param active_shows: The active_shows of this LampStateAllOf.  # noqa: E501
        :type active_shows: list[int]
        """

        self._active_shows = active_shows

    @property
    def start_state(self):
        """Gets the start_state of this LampStateAllOf.  # noqa: E501


        :return: The start_state of this LampStateAllOf.  # noqa: E501
        :rtype: LampStateParameters
        """
        return self._start_state

    @start_state.setter
    def start_state(self, start_state):
        """Sets the start_state of this LampStateAllOf.


        :param start_state: The start_state of this LampStateAllOf.  # noqa: E501
        :type start_state: LampStateParameters
        """

        self._start_state = start_state

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
        if not isinstance(other, LampStateAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LampStateAllOf):
            return True

        return self.to_dict() != other.to_dict()
