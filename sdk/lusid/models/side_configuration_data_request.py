# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2306
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class SideConfigurationDataRequest(object):
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
        'side': 'str',
        'security': 'str',
        'currency': 'str',
        'rate': 'str',
        'units': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'side': 'side',
        'security': 'security',
        'currency': 'currency',
        'rate': 'rate',
        'units': 'units',
        'amount': 'amount'
    }

    required_map = {
        'side': 'required',
        'security': 'required',
        'currency': 'required',
        'rate': 'required',
        'units': 'required',
        'amount': 'required'
    }

    def __init__(self, side=None, security=None, currency=None, rate=None, units=None, amount=None):  # noqa: E501
        """
        SideConfigurationDataRequest - a model defined in OpenAPI

        :param side:  The side's label. (required)
        :type side: str
        :param security:  The security, or instrument. (required)
        :type security: str
        :param currency:  The currency. (required)
        :type currency: str
        :param rate:  The rate. (required)
        :type rate: str
        :param units:  The units. (required)
        :type units: str
        :param amount:  The amount. (required)
        :type amount: str

        """  # noqa: E501

        self._side = None
        self._security = None
        self._currency = None
        self._rate = None
        self._units = None
        self._amount = None
        self.discriminator = None

        self.side = side
        self.security = security
        self.currency = currency
        self.rate = rate
        self.units = units
        self.amount = amount

    @property
    def side(self):
        """Gets the side of this SideConfigurationDataRequest.  # noqa: E501

        The side's label.  # noqa: E501

        :return: The side of this SideConfigurationDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this SideConfigurationDataRequest.

        The side's label.  # noqa: E501

        :param side: The side of this SideConfigurationDataRequest.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def security(self):
        """Gets the security of this SideConfigurationDataRequest.  # noqa: E501

        The security, or instrument.  # noqa: E501

        :return: The security of this SideConfigurationDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this SideConfigurationDataRequest.

        The security, or instrument.  # noqa: E501

        :param security: The security of this SideConfigurationDataRequest.  # noqa: E501
        :type: str
        """
        if security is None:
            raise ValueError("Invalid value for `security`, must not be `None`")  # noqa: E501

        self._security = security

    @property
    def currency(self):
        """Gets the currency of this SideConfigurationDataRequest.  # noqa: E501

        The currency.  # noqa: E501

        :return: The currency of this SideConfigurationDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SideConfigurationDataRequest.

        The currency.  # noqa: E501

        :param currency: The currency of this SideConfigurationDataRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def rate(self):
        """Gets the rate of this SideConfigurationDataRequest.  # noqa: E501

        The rate.  # noqa: E501

        :return: The rate of this SideConfigurationDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this SideConfigurationDataRequest.

        The rate.  # noqa: E501

        :param rate: The rate of this SideConfigurationDataRequest.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def units(self):
        """Gets the units of this SideConfigurationDataRequest.  # noqa: E501

        The units.  # noqa: E501

        :return: The units of this SideConfigurationDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this SideConfigurationDataRequest.

        The units.  # noqa: E501

        :param units: The units of this SideConfigurationDataRequest.  # noqa: E501
        :type: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def amount(self):
        """Gets the amount of this SideConfigurationDataRequest.  # noqa: E501

        The amount.  # noqa: E501

        :return: The amount of this SideConfigurationDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SideConfigurationDataRequest.

        The amount.  # noqa: E501

        :param amount: The amount of this SideConfigurationDataRequest.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if not isinstance(other, SideConfigurationDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
