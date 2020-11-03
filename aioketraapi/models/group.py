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


class Group(object):
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
        'id': 'str',
        'name': 'str',
        'child_groups': 'list[str]',
        'parent_groups': 'list[str]',
        'address': 'int',
        'state': 'LampState'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'child_groups': 'ChildGroups',
        'parent_groups': 'ParentGroups',
        'address': 'Address',
        'state': 'State'
    }

    def __init__(self, id=None, name=None, child_groups=None, parent_groups=None, address=None, state=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._child_groups = None
        self._parent_groups = None
        self._address = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if child_groups is not None:
            self.child_groups = child_groups
        if parent_groups is not None:
            self.parent_groups = parent_groups
        if address is not None:
            self.address = address
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        Unique id of the group  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        Unique id of the group  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        Name of the group  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        Name of the group  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def child_groups(self):
        """Gets the child_groups of this Group.  # noqa: E501

        Ids of child groups of this group.  Added in API Schema 4 (firmware version 1.15).  For this to be populated, the hub must be published with Design Studio 2.0 and the SupportsZoneKeypads property returned in GET /Hub must be true.  See the API overview document for more explanation.  # noqa: E501

        :return: The child_groups of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._child_groups

    @child_groups.setter
    def child_groups(self, child_groups):
        """Sets the child_groups of this Group.

        Ids of child groups of this group.  Added in API Schema 4 (firmware version 1.15).  For this to be populated, the hub must be published with Design Studio 2.0 and the SupportsZoneKeypads property returned in GET /Hub must be true.  See the API overview document for more explanation.  # noqa: E501

        :param child_groups: The child_groups of this Group.  # noqa: E501
        :type child_groups: list[str]
        """

        self._child_groups = child_groups

    @property
    def parent_groups(self):
        """Gets the parent_groups of this Group.  # noqa: E501

        Ids of parent groups of this group.  Added in API Schema 4 (firmware version 1.15).  For this to be populated, the hub must be published with Design Studio 2.0 and the SupportsZoneKeypads property returned in GET /Hub must be true.  See the API overview document for more explanation.  # noqa: E501

        :return: The parent_groups of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_groups

    @parent_groups.setter
    def parent_groups(self, parent_groups):
        """Sets the parent_groups of this Group.

        Ids of parent groups of this group.  Added in API Schema 4 (firmware version 1.15).  For this to be populated, the hub must be published with Design Studio 2.0 and the SupportsZoneKeypads property returned in GET /Hub must be true.  See the API overview document for more explanation.  # noqa: E501

        :param parent_groups: The parent_groups of this Group.  # noqa: E501
        :type parent_groups: list[str]
        """

        self._parent_groups = parent_groups

    @property
    def address(self):
        """Gets the address of this Group.  # noqa: E501

        The logical address of the group.  Added in API Schema 4 (firmware version 1.15)  # noqa: E501

        :return: The address of this Group.  # noqa: E501
        :rtype: int
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Group.

        The logical address of the group.  Added in API Schema 4 (firmware version 1.15)  # noqa: E501

        :param address: The address of this Group.  # noqa: E501
        :type address: int
        """

        self._address = address

    @property
    def state(self):
        """Gets the state of this Group.  # noqa: E501


        :return: The state of this Group.  # noqa: E501
        :rtype: LampState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Group.


        :param state: The state of this Group.  # noqa: E501
        :type state: LampState
        """

        self._state = state

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
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()
