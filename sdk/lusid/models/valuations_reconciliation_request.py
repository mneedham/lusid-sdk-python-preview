# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2998
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ValuationsReconciliationRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'left': 'ValuationRequest',
        'right': 'ValuationRequest',
        'left_to_right_mapping': 'list[ReconciliationLeftRightAddressKeyPair]',
        'preserve_keys': 'list[str]'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'left_to_right_mapping': 'leftToRightMapping',
        'preserve_keys': 'preserveKeys'
    }

    required_map = {
        'left': 'required',
        'right': 'required',
        'left_to_right_mapping': 'optional',
        'preserve_keys': 'optional'
    }

    def __init__(self, left=None, right=None, left_to_right_mapping=None, preserve_keys=None):  # noqa: E501
        """
        ValuationsReconciliationRequest - a model defined in OpenAPI

        :param left:  (required)
        :type left: lusid.ValuationRequest
        :param right:  (required)
        :type right: lusid.ValuationRequest
        :param left_to_right_mapping:  The mapping from property keys requested by left aggregation to property keys on right hand side
        :type left_to_right_mapping: list[lusid.ReconciliationLeftRightAddressKeyPair]
        :param preserve_keys:  List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping
        :type preserve_keys: list[str]

        """  # noqa: E501

        self._left = None
        self._right = None
        self._left_to_right_mapping = None
        self._preserve_keys = None
        self.discriminator = None

        self.left = left
        self.right = right
        self.left_to_right_mapping = left_to_right_mapping
        self.preserve_keys = preserve_keys

    @property
    def left(self):
        """Gets the left of this ValuationsReconciliationRequest.  # noqa: E501


        :return: The left of this ValuationsReconciliationRequest.  # noqa: E501
        :rtype: ValuationRequest
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ValuationsReconciliationRequest.


        :param left: The left of this ValuationsReconciliationRequest.  # noqa: E501
        :type: ValuationRequest
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def right(self):
        """Gets the right of this ValuationsReconciliationRequest.  # noqa: E501


        :return: The right of this ValuationsReconciliationRequest.  # noqa: E501
        :rtype: ValuationRequest
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this ValuationsReconciliationRequest.


        :param right: The right of this ValuationsReconciliationRequest.  # noqa: E501
        :type: ValuationRequest
        """
        if right is None:
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501

        self._right = right

    @property
    def left_to_right_mapping(self):
        """Gets the left_to_right_mapping of this ValuationsReconciliationRequest.  # noqa: E501

        The mapping from property keys requested by left aggregation to property keys on right hand side  # noqa: E501

        :return: The left_to_right_mapping of this ValuationsReconciliationRequest.  # noqa: E501
        :rtype: list[ReconciliationLeftRightAddressKeyPair]
        """
        return self._left_to_right_mapping

    @left_to_right_mapping.setter
    def left_to_right_mapping(self, left_to_right_mapping):
        """Sets the left_to_right_mapping of this ValuationsReconciliationRequest.

        The mapping from property keys requested by left aggregation to property keys on right hand side  # noqa: E501

        :param left_to_right_mapping: The left_to_right_mapping of this ValuationsReconciliationRequest.  # noqa: E501
        :type: list[ReconciliationLeftRightAddressKeyPair]
        """

        self._left_to_right_mapping = left_to_right_mapping

    @property
    def preserve_keys(self):
        """Gets the preserve_keys of this ValuationsReconciliationRequest.  # noqa: E501

        List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping  # noqa: E501

        :return: The preserve_keys of this ValuationsReconciliationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._preserve_keys

    @preserve_keys.setter
    def preserve_keys(self, preserve_keys):
        """Sets the preserve_keys of this ValuationsReconciliationRequest.

        List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping  # noqa: E501

        :param preserve_keys: The preserve_keys of this ValuationsReconciliationRequest.  # noqa: E501
        :type: list[str]
        """

        self._preserve_keys = preserve_keys

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
        if not isinstance(other, ValuationsReconciliationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
