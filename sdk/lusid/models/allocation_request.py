# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3192
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AllocationRequest(object):
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
        'portfolio_id': 'ResourceId',
        'allocated_order_id': 'ResourceId',
        'id': 'ResourceId',
        'placement_ids': 'list[ResourceId]',
        'state': 'str',
        'side': 'str',
        'type': 'str',
        'settlement_date': 'datetime',
        'date': 'datetime',
        'price': 'CurrencyAndAmount',
        'settlement_currency': 'str',
        'settlement_currency_fx_rate': 'float',
        'counterparty': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'instrument_identifiers': 'instrumentIdentifiers',
        'quantity': 'quantity',
        'portfolio_id': 'portfolioId',
        'allocated_order_id': 'allocatedOrderId',
        'id': 'id',
        'placement_ids': 'placementIds',
        'state': 'state',
        'side': 'side',
        'type': 'type',
        'settlement_date': 'settlementDate',
        'date': 'date',
        'price': 'price',
        'settlement_currency': 'settlementCurrency',
        'settlement_currency_fx_rate': 'settlementCurrencyFxRate',
        'counterparty': 'counterparty'
    }

    required_map = {
        'properties': 'optional',
        'instrument_identifiers': 'required',
        'quantity': 'required',
        'portfolio_id': 'required',
        'allocated_order_id': 'required',
        'id': 'required',
        'placement_ids': 'optional',
        'state': 'optional',
        'side': 'optional',
        'type': 'optional',
        'settlement_date': 'optional',
        'date': 'optional',
        'price': 'optional',
        'settlement_currency': 'optional',
        'settlement_currency_fx_rate': 'optional',
        'counterparty': 'optional'
    }

    def __init__(self, properties=None, instrument_identifiers=None, quantity=None, portfolio_id=None, allocated_order_id=None, id=None, placement_ids=None, state=None, side=None, type=None, settlement_date=None, date=None, price=None, settlement_currency=None, settlement_currency_fx_rate=None, counterparty=None):  # noqa: E501
        """
        AllocationRequest - a model defined in OpenAPI

        :param properties:  Client-defined properties associated with this allocation.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param instrument_identifiers:  The instrument allocated. (required)
        :type instrument_identifiers: dict(str, str)
        :param quantity:  The quantity of given instrument allocated. (required)
        :type quantity: int
        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param allocated_order_id:  (required)
        :type allocated_order_id: lusid.ResourceId
        :param id:  (required)
        :type id: lusid.ResourceId
        :param placement_ids:  A placement - also known as an order placed in the market - associated with this allocation.
        :type placement_ids: list[lusid.ResourceId]
        :param state:  The state of this allocation.
        :type state: str
        :param side:  The side of this allocation (examples: Buy, Sell, ...).
        :type side: str
        :param type:  The type of order associated with this allocation (examples: Limit, Market, ...).
        :type type: str
        :param settlement_date:  The settlement date for this allocation.
        :type settlement_date: datetime
        :param date:  The date of this allocation.
        :type date: datetime
        :param price: 
        :type price: lusid.CurrencyAndAmount
        :param settlement_currency:  The settlement currency of this allocation.
        :type settlement_currency: str
        :param settlement_currency_fx_rate:  The settlement currency to allocation currency FX rate.
        :type settlement_currency_fx_rate: float
        :param counterparty:  The counterparty for this allocation.
        :type counterparty: str

        """  # noqa: E501

        self._properties = None
        self._instrument_identifiers = None
        self._quantity = None
        self._portfolio_id = None
        self._allocated_order_id = None
        self._id = None
        self._placement_ids = None
        self._state = None
        self._side = None
        self._type = None
        self._settlement_date = None
        self._date = None
        self._price = None
        self._settlement_currency = None
        self._settlement_currency_fx_rate = None
        self._counterparty = None
        self.discriminator = None

        self.properties = properties
        self.instrument_identifiers = instrument_identifiers
        self.quantity = quantity
        self.portfolio_id = portfolio_id
        self.allocated_order_id = allocated_order_id
        self.id = id
        self.placement_ids = placement_ids
        self.state = state
        self.side = side
        self.type = type
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if date is not None:
            self.date = date
        if price is not None:
            self.price = price
        self.settlement_currency = settlement_currency
        if settlement_currency_fx_rate is not None:
            self.settlement_currency_fx_rate = settlement_currency_fx_rate
        self.counterparty = counterparty

    @property
    def properties(self):
        """Gets the properties of this AllocationRequest.  # noqa: E501

        Client-defined properties associated with this allocation.  # noqa: E501

        :return: The properties of this AllocationRequest.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AllocationRequest.

        Client-defined properties associated with this allocation.  # noqa: E501

        :param properties: The properties of this AllocationRequest.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this AllocationRequest.  # noqa: E501

        The instrument allocated.  # noqa: E501

        :return: The instrument_identifiers of this AllocationRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this AllocationRequest.

        The instrument allocated.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this AllocationRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if instrument_identifiers is None:
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def quantity(self):
        """Gets the quantity of this AllocationRequest.  # noqa: E501

        The quantity of given instrument allocated.  # noqa: E501

        :return: The quantity of this AllocationRequest.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this AllocationRequest.

        The quantity of given instrument allocated.  # noqa: E501

        :param quantity: The quantity of this AllocationRequest.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this AllocationRequest.  # noqa: E501


        :return: The portfolio_id of this AllocationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this AllocationRequest.


        :param portfolio_id: The portfolio_id of this AllocationRequest.  # noqa: E501
        :type: ResourceId
        """
        if portfolio_id is None:
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def allocated_order_id(self):
        """Gets the allocated_order_id of this AllocationRequest.  # noqa: E501


        :return: The allocated_order_id of this AllocationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._allocated_order_id

    @allocated_order_id.setter
    def allocated_order_id(self, allocated_order_id):
        """Sets the allocated_order_id of this AllocationRequest.


        :param allocated_order_id: The allocated_order_id of this AllocationRequest.  # noqa: E501
        :type: ResourceId
        """
        if allocated_order_id is None:
            raise ValueError("Invalid value for `allocated_order_id`, must not be `None`")  # noqa: E501

        self._allocated_order_id = allocated_order_id

    @property
    def id(self):
        """Gets the id of this AllocationRequest.  # noqa: E501


        :return: The id of this AllocationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllocationRequest.


        :param id: The id of this AllocationRequest.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def placement_ids(self):
        """Gets the placement_ids of this AllocationRequest.  # noqa: E501

        A placement - also known as an order placed in the market - associated with this allocation.  # noqa: E501

        :return: The placement_ids of this AllocationRequest.  # noqa: E501
        :rtype: list[ResourceId]
        """
        return self._placement_ids

    @placement_ids.setter
    def placement_ids(self, placement_ids):
        """Sets the placement_ids of this AllocationRequest.

        A placement - also known as an order placed in the market - associated with this allocation.  # noqa: E501

        :param placement_ids: The placement_ids of this AllocationRequest.  # noqa: E501
        :type: list[ResourceId]
        """

        self._placement_ids = placement_ids

    @property
    def state(self):
        """Gets the state of this AllocationRequest.  # noqa: E501

        The state of this allocation.  # noqa: E501

        :return: The state of this AllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AllocationRequest.

        The state of this allocation.  # noqa: E501

        :param state: The state of this AllocationRequest.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def side(self):
        """Gets the side of this AllocationRequest.  # noqa: E501

        The side of this allocation (examples: Buy, Sell, ...).  # noqa: E501

        :return: The side of this AllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this AllocationRequest.

        The side of this allocation (examples: Buy, Sell, ...).  # noqa: E501

        :param side: The side of this AllocationRequest.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def type(self):
        """Gets the type of this AllocationRequest.  # noqa: E501

        The type of order associated with this allocation (examples: Limit, Market, ...).  # noqa: E501

        :return: The type of this AllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AllocationRequest.

        The type of order associated with this allocation (examples: Limit, Market, ...).  # noqa: E501

        :param type: The type of this AllocationRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def settlement_date(self):
        """Gets the settlement_date of this AllocationRequest.  # noqa: E501

        The settlement date for this allocation.  # noqa: E501

        :return: The settlement_date of this AllocationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this AllocationRequest.

        The settlement date for this allocation.  # noqa: E501

        :param settlement_date: The settlement_date of this AllocationRequest.  # noqa: E501
        :type: datetime
        """

        self._settlement_date = settlement_date

    @property
    def date(self):
        """Gets the date of this AllocationRequest.  # noqa: E501

        The date of this allocation.  # noqa: E501

        :return: The date of this AllocationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AllocationRequest.

        The date of this allocation.  # noqa: E501

        :param date: The date of this AllocationRequest.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def price(self):
        """Gets the price of this AllocationRequest.  # noqa: E501


        :return: The price of this AllocationRequest.  # noqa: E501
        :rtype: CurrencyAndAmount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AllocationRequest.


        :param price: The price of this AllocationRequest.  # noqa: E501
        :type: CurrencyAndAmount
        """

        self._price = price

    @property
    def settlement_currency(self):
        """Gets the settlement_currency of this AllocationRequest.  # noqa: E501

        The settlement currency of this allocation.  # noqa: E501

        :return: The settlement_currency of this AllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """Sets the settlement_currency of this AllocationRequest.

        The settlement currency of this allocation.  # noqa: E501

        :param settlement_currency: The settlement_currency of this AllocationRequest.  # noqa: E501
        :type: str
        """

        self._settlement_currency = settlement_currency

    @property
    def settlement_currency_fx_rate(self):
        """Gets the settlement_currency_fx_rate of this AllocationRequest.  # noqa: E501

        The settlement currency to allocation currency FX rate.  # noqa: E501

        :return: The settlement_currency_fx_rate of this AllocationRequest.  # noqa: E501
        :rtype: float
        """
        return self._settlement_currency_fx_rate

    @settlement_currency_fx_rate.setter
    def settlement_currency_fx_rate(self, settlement_currency_fx_rate):
        """Sets the settlement_currency_fx_rate of this AllocationRequest.

        The settlement currency to allocation currency FX rate.  # noqa: E501

        :param settlement_currency_fx_rate: The settlement_currency_fx_rate of this AllocationRequest.  # noqa: E501
        :type: float
        """

        self._settlement_currency_fx_rate = settlement_currency_fx_rate

    @property
    def counterparty(self):
        """Gets the counterparty of this AllocationRequest.  # noqa: E501

        The counterparty for this allocation.  # noqa: E501

        :return: The counterparty of this AllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this AllocationRequest.

        The counterparty for this allocation.  # noqa: E501

        :param counterparty: The counterparty of this AllocationRequest.  # noqa: E501
        :type: str
        """

        self._counterparty = counterparty

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
        if not isinstance(other, AllocationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
