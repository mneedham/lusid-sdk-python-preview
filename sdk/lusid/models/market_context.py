# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3158
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MarketContext(object):
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
        'market_rules': 'list[MarketDataKeyRule]',
        'suppliers': 'MarketContextSuppliers',
        'options': 'MarketOptions'
    }

    attribute_map = {
        'market_rules': 'marketRules',
        'suppliers': 'suppliers',
        'options': 'options'
    }

    required_map = {
        'market_rules': 'optional',
        'suppliers': 'optional',
        'options': 'optional'
    }

    def __init__(self, market_rules=None, suppliers=None, options=None):  # noqa: E501
        """
        MarketContext - a model defined in OpenAPI

        :param market_rules:  The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.
        :type market_rules: list[lusid.MarketDataKeyRule]
        :param suppliers: 
        :type suppliers: lusid.MarketContextSuppliers
        :param options: 
        :type options: lusid.MarketOptions

        """  # noqa: E501

        self._market_rules = None
        self._suppliers = None
        self._options = None
        self.discriminator = None

        self.market_rules = market_rules
        self.suppliers = suppliers
        if options is not None:
            self.options = options

    @property
    def market_rules(self):
        """Gets the market_rules of this MarketContext.  # noqa: E501

        The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.  # noqa: E501

        :return: The market_rules of this MarketContext.  # noqa: E501
        :rtype: list[MarketDataKeyRule]
        """
        return self._market_rules

    @market_rules.setter
    def market_rules(self, market_rules):
        """Sets the market_rules of this MarketContext.

        The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.  # noqa: E501

        :param market_rules: The market_rules of this MarketContext.  # noqa: E501
        :type: list[MarketDataKeyRule]
        """

        self._market_rules = market_rules

    @property
    def suppliers(self):
        """Gets the suppliers of this MarketContext.  # noqa: E501


        :return: The suppliers of this MarketContext.  # noqa: E501
        :rtype: MarketContextSuppliers
        """
        return self._suppliers

    @suppliers.setter
    def suppliers(self, suppliers):
        """Sets the suppliers of this MarketContext.


        :param suppliers: The suppliers of this MarketContext.  # noqa: E501
        :type: MarketContextSuppliers
        """

        self._suppliers = suppliers

    @property
    def options(self):
        """Gets the options of this MarketContext.  # noqa: E501


        :return: The options of this MarketContext.  # noqa: E501
        :rtype: MarketOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MarketContext.


        :param options: The options of this MarketContext.  # noqa: E501
        :type: MarketOptions
        """

        self._options = options

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
        if not isinstance(other, MarketContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
