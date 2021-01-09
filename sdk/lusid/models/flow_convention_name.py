# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2452
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class FlowConventionName(object):
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
        'currency': 'str',
        'index_name': 'str',
        'tenor': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'index_name': 'indexName',
        'tenor': 'tenor'
    }

    required_map = {
        'currency': 'required',
        'index_name': 'optional',
        'tenor': 'required'
    }

    def __init__(self, currency=None, index_name=None, tenor=None):  # noqa: E501
        """
        FlowConventionName - a model defined in OpenAPI

        :param currency:  Currency of the flow convention name. (required)
        :type currency: str
        :param index_name:  The index, if present, that is required. e.g. \"IBOR\", \"OIS\" or \"SONIA\".
        :type index_name: str
        :param tenor:  Tenor for the convention name (required)
        :type tenor: str

        """  # noqa: E501

        self._currency = None
        self._index_name = None
        self._tenor = None
        self.discriminator = None

        self.currency = currency
        self.index_name = index_name
        self.tenor = tenor

    @property
    def currency(self):
        """Gets the currency of this FlowConventionName.  # noqa: E501

        Currency of the flow convention name.  # noqa: E501

        :return: The currency of this FlowConventionName.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FlowConventionName.

        Currency of the flow convention name.  # noqa: E501

        :param currency: The currency of this FlowConventionName.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def index_name(self):
        """Gets the index_name of this FlowConventionName.  # noqa: E501

        The index, if present, that is required. e.g. \"IBOR\", \"OIS\" or \"SONIA\".  # noqa: E501

        :return: The index_name of this FlowConventionName.  # noqa: E501
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this FlowConventionName.

        The index, if present, that is required. e.g. \"IBOR\", \"OIS\" or \"SONIA\".  # noqa: E501

        :param index_name: The index_name of this FlowConventionName.  # noqa: E501
        :type: str
        """

        self._index_name = index_name

    @property
    def tenor(self):
        """Gets the tenor of this FlowConventionName.  # noqa: E501

        Tenor for the convention name  # noqa: E501

        :return: The tenor of this FlowConventionName.  # noqa: E501
        :rtype: str
        """
        return self._tenor

    @tenor.setter
    def tenor(self, tenor):
        """Sets the tenor of this FlowConventionName.

        Tenor for the convention name  # noqa: E501

        :param tenor: The tenor of this FlowConventionName.  # noqa: E501
        :type: str
        """
        if tenor is None:
            raise ValueError("Invalid value for `tenor`, must not be `None`")  # noqa: E501

        self._tenor = tenor

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
        if not isinstance(other, FlowConventionName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
