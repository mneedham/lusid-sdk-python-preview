# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2789
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ResultDataSchema(object):
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
        'node_value_schema': 'dict(str, FieldSchema)',
        'property_schema': 'dict(str, FieldSchema)'
    }

    attribute_map = {
        'node_value_schema': 'nodeValueSchema',
        'property_schema': 'propertySchema'
    }

    required_map = {
        'node_value_schema': 'optional',
        'property_schema': 'optional'
    }

    def __init__(self, node_value_schema=None, property_schema=None):  # noqa: E501
        """
        ResultDataSchema - a model defined in OpenAPI

        :param node_value_schema: 
        :type node_value_schema: dict[str, lusid.FieldSchema]
        :param property_schema: 
        :type property_schema: dict[str, lusid.FieldSchema]

        """  # noqa: E501

        self._node_value_schema = None
        self._property_schema = None
        self.discriminator = None

        self.node_value_schema = node_value_schema
        self.property_schema = property_schema

    @property
    def node_value_schema(self):
        """Gets the node_value_schema of this ResultDataSchema.  # noqa: E501


        :return: The node_value_schema of this ResultDataSchema.  # noqa: E501
        :rtype: dict(str, FieldSchema)
        """
        return self._node_value_schema

    @node_value_schema.setter
    def node_value_schema(self, node_value_schema):
        """Sets the node_value_schema of this ResultDataSchema.


        :param node_value_schema: The node_value_schema of this ResultDataSchema.  # noqa: E501
        :type: dict(str, FieldSchema)
        """

        self._node_value_schema = node_value_schema

    @property
    def property_schema(self):
        """Gets the property_schema of this ResultDataSchema.  # noqa: E501


        :return: The property_schema of this ResultDataSchema.  # noqa: E501
        :rtype: dict(str, FieldSchema)
        """
        return self._property_schema

    @property_schema.setter
    def property_schema(self, property_schema):
        """Sets the property_schema of this ResultDataSchema.


        :param property_schema: The property_schema of this ResultDataSchema.  # noqa: E501
        :type: dict(str, FieldSchema)
        """

        self._property_schema = property_schema

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
        if not isinstance(other, ResultDataSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
