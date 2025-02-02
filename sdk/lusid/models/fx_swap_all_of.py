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

class FxSwapAllOf(object):
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
        'near_fx_forward': 'FxForward',
        'far_fx_forward': 'FxForward',
        'instrument_type': 'str'
    }

    attribute_map = {
        'near_fx_forward': 'nearFxForward',
        'far_fx_forward': 'farFxForward',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'near_fx_forward': 'required',
        'far_fx_forward': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, near_fx_forward=None, far_fx_forward=None, instrument_type=None):  # noqa: E501
        """
        FxSwapAllOf - a model defined in OpenAPI

        :param near_fx_forward:  (required)
        :type near_fx_forward: lusid.FxForward
        :param far_fx_forward:  (required)
        :type far_fx_forward: lusid.FxForward
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap (required)
        :type instrument_type: str

        """  # noqa: E501

        self._near_fx_forward = None
        self._far_fx_forward = None
        self._instrument_type = None
        self.discriminator = None

        self.near_fx_forward = near_fx_forward
        self.far_fx_forward = far_fx_forward
        self.instrument_type = instrument_type

    @property
    def near_fx_forward(self):
        """Gets the near_fx_forward of this FxSwapAllOf.  # noqa: E501


        :return: The near_fx_forward of this FxSwapAllOf.  # noqa: E501
        :rtype: FxForward
        """
        return self._near_fx_forward

    @near_fx_forward.setter
    def near_fx_forward(self, near_fx_forward):
        """Sets the near_fx_forward of this FxSwapAllOf.


        :param near_fx_forward: The near_fx_forward of this FxSwapAllOf.  # noqa: E501
        :type: FxForward
        """
        if near_fx_forward is None:
            raise ValueError("Invalid value for `near_fx_forward`, must not be `None`")  # noqa: E501

        self._near_fx_forward = near_fx_forward

    @property
    def far_fx_forward(self):
        """Gets the far_fx_forward of this FxSwapAllOf.  # noqa: E501


        :return: The far_fx_forward of this FxSwapAllOf.  # noqa: E501
        :rtype: FxForward
        """
        return self._far_fx_forward

    @far_fx_forward.setter
    def far_fx_forward(self, far_fx_forward):
        """Sets the far_fx_forward of this FxSwapAllOf.


        :param far_fx_forward: The far_fx_forward of this FxSwapAllOf.  # noqa: E501
        :type: FxForward
        """
        if far_fx_forward is None:
            raise ValueError("Invalid value for `far_fx_forward`, must not be `None`")  # noqa: E501

        self._far_fx_forward = far_fx_forward

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FxSwapAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap  # noqa: E501

        :return: The instrument_type of this FxSwapAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FxSwapAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap  # noqa: E501

        :param instrument_type: The instrument_type of this FxSwapAllOf.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap"]  # noqa: E501
        if instrument_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, FxSwapAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
