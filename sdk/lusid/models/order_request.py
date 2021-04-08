# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2830
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class OrderRequest(object):
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
        'properties': 'dict(str, PerpetualProperty)',
        'instrument_identifiers': 'dict(str, str)',
        'quantity': 'int',
        'side': 'str',
        'order_book_id': 'ResourceId',
        'portfolio_id': 'ResourceId',
        'id': 'ResourceId'
    }

    attribute_map = {
        'properties': 'properties',
        'instrument_identifiers': 'instrumentIdentifiers',
        'quantity': 'quantity',
        'side': 'side',
        'order_book_id': 'orderBookId',
        'portfolio_id': 'portfolioId',
        'id': 'id'
    }

    required_map = {
        'properties': 'optional',
        'instrument_identifiers': 'required',
        'quantity': 'required',
        'side': 'required',
        'order_book_id': 'required',
        'portfolio_id': 'required',
        'id': 'required'
    }

    def __init__(self, properties=None, instrument_identifiers=None, quantity=None, side=None, order_book_id=None, portfolio_id=None, id=None):  # noqa: E501
        """
        OrderRequest - a model defined in OpenAPI

        :param properties:  Client-defined properties associated with this order.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param quantity:  The quantity of given instrument ordered. (required)
        :type quantity: int
        :param side:  The client's representation of the order's side (buy, sell, short, etc) (required)
        :type side: str
        :param order_book_id:  (required)
        :type order_book_id: lusid.ResourceId
        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param id:  (required)
        :type id: lusid.ResourceId

        """  # noqa: E501

        self._properties = None
        self._instrument_identifiers = None
        self._quantity = None
        self._side = None
        self._order_book_id = None
        self._portfolio_id = None
        self._id = None
        self.discriminator = None

        self.properties = properties
        self.instrument_identifiers = instrument_identifiers
        self.quantity = quantity
        self.side = side
        self.order_book_id = order_book_id
        self.portfolio_id = portfolio_id
        self.id = id

    @property
    def properties(self):
        """Gets the properties of this OrderRequest.  # noqa: E501

        Client-defined properties associated with this order.  # noqa: E501

        :return: The properties of this OrderRequest.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this OrderRequest.

        Client-defined properties associated with this order.  # noqa: E501

        :param properties: The properties of this OrderRequest.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this OrderRequest.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this OrderRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this OrderRequest.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this OrderRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if instrument_identifiers is None:
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def quantity(self):
        """Gets the quantity of this OrderRequest.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this OrderRequest.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderRequest.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this OrderRequest.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def side(self):
        """Gets the side of this OrderRequest.  # noqa: E501

        The client's representation of the order's side (buy, sell, short, etc)  # noqa: E501

        :return: The side of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OrderRequest.

        The client's representation of the order's side (buy, sell, short, etc)  # noqa: E501

        :param side: The side of this OrderRequest.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def order_book_id(self):
        """Gets the order_book_id of this OrderRequest.  # noqa: E501


        :return: The order_book_id of this OrderRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._order_book_id

    @order_book_id.setter
    def order_book_id(self, order_book_id):
        """Sets the order_book_id of this OrderRequest.


        :param order_book_id: The order_book_id of this OrderRequest.  # noqa: E501
        :type: ResourceId
        """
        if order_book_id is None:
            raise ValueError("Invalid value for `order_book_id`, must not be `None`")  # noqa: E501

        self._order_book_id = order_book_id

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this OrderRequest.  # noqa: E501


        :return: The portfolio_id of this OrderRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this OrderRequest.


        :param portfolio_id: The portfolio_id of this OrderRequest.  # noqa: E501
        :type: ResourceId
        """
        if portfolio_id is None:
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def id(self):
        """Gets the id of this OrderRequest.  # noqa: E501


        :return: The id of this OrderRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderRequest.


        :param id: The id of this OrderRequest.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, OrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
