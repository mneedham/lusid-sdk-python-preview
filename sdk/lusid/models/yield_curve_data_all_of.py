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

class YieldCurveDataAllOf(object):
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
        'base_date': 'datetime',
        'instruments': 'list[LusidInstrument]',
        'quotes': 'list[MarketQuote]',
        'market_data_type': 'str'
    }

    attribute_map = {
        'base_date': 'baseDate',
        'instruments': 'instruments',
        'quotes': 'quotes',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'base_date': 'required',
        'instruments': 'required',
        'quotes': 'required',
        'market_data_type': 'required'
    }

    def __init__(self, base_date=None, instruments=None, quotes=None, market_data_type=None):  # noqa: E501
        """
        YieldCurveDataAllOf - a model defined in OpenAPI

        :param base_date:  Base date (required)
        :type base_date: datetime
        :param instruments:  The set of instruments that define the curve. (required)
        :type instruments: list[lusid.LusidInstrument]
        :param quotes:  The market quotes corresponding to the the instruments used to define the curve (required)
        :type quotes: list[lusid.MarketQuote]
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData (required)
        :type market_data_type: str

        """  # noqa: E501

        self._base_date = None
        self._instruments = None
        self._quotes = None
        self._market_data_type = None
        self.discriminator = None

        self.base_date = base_date
        self.instruments = instruments
        self.quotes = quotes
        self.market_data_type = market_data_type

    @property
    def base_date(self):
        """Gets the base_date of this YieldCurveDataAllOf.  # noqa: E501

        Base date  # noqa: E501

        :return: The base_date of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this YieldCurveDataAllOf.

        Base date  # noqa: E501

        :param base_date: The base_date of this YieldCurveDataAllOf.  # noqa: E501
        :type: datetime
        """
        if base_date is None:
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def instruments(self):
        """Gets the instruments of this YieldCurveDataAllOf.  # noqa: E501

        The set of instruments that define the curve.  # noqa: E501

        :return: The instruments of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: list[LusidInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this YieldCurveDataAllOf.

        The set of instruments that define the curve.  # noqa: E501

        :param instruments: The instruments of this YieldCurveDataAllOf.  # noqa: E501
        :type: list[LusidInstrument]
        """
        if instruments is None:
            raise ValueError("Invalid value for `instruments`, must not be `None`")  # noqa: E501

        self._instruments = instruments

    @property
    def quotes(self):
        """Gets the quotes of this YieldCurveDataAllOf.  # noqa: E501

        The market quotes corresponding to the the instruments used to define the curve  # noqa: E501

        :return: The quotes of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: list[MarketQuote]
        """
        return self._quotes

    @quotes.setter
    def quotes(self, quotes):
        """Sets the quotes of this YieldCurveDataAllOf.

        The market quotes corresponding to the the instruments used to define the curve  # noqa: E501

        :param quotes: The quotes of this YieldCurveDataAllOf.  # noqa: E501
        :type: list[MarketQuote]
        """
        if quotes is None:
            raise ValueError("Invalid value for `quotes`, must not be `None`")  # noqa: E501

        self._quotes = quotes

    @property
    def market_data_type(self):
        """Gets the market_data_type of this YieldCurveDataAllOf.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData  # noqa: E501

        :return: The market_data_type of this YieldCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this YieldCurveDataAllOf.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData  # noqa: E501

        :param market_data_type: The market_data_type of this YieldCurveDataAllOf.  # noqa: E501
        :type: str
        """
        if market_data_type is None:
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData"]  # noqa: E501
        if market_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `market_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_type, allowed_values)
            )

        self._market_data_type = market_data_type

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
        if not isinstance(other, YieldCurveDataAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
