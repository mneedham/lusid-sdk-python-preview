# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2347
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ExoticInstrument(object):
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
        'instrument_format': 'InstrumentDefinitionFormat',
        'content': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'instrument_format': 'instrumentFormat',
        'content': 'content',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'instrument_format': 'required',
        'content': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, instrument_format=None, content=None, instrument_type=None):  # noqa: E501
        """
        ExoticInstrument - a model defined in OpenAPI

        :param instrument_format:  (required)
        :type instrument_format: lusid.InstrumentDefinitionFormat
        :param content:  The original document received into the system. This format could potentially be anything though is most likely to be either Json or Xml. In the case where no other              interface is supported it is possible to fall back onto this.              For example, a trade from an external client system. This may be recognized internally by Lusid or simply passed through to another vendor system. (required)
        :type content: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit (required)
        :type instrument_type: str

        """  # noqa: E501

        self._instrument_format = None
        self._content = None
        self._instrument_type = None
        self.discriminator = None

        self.instrument_format = instrument_format
        self.content = content
        self.instrument_type = instrument_type

    @property
    def instrument_format(self):
        """Gets the instrument_format of this ExoticInstrument.  # noqa: E501


        :return: The instrument_format of this ExoticInstrument.  # noqa: E501
        :rtype: InstrumentDefinitionFormat
        """
        return self._instrument_format

    @instrument_format.setter
    def instrument_format(self, instrument_format):
        """Sets the instrument_format of this ExoticInstrument.


        :param instrument_format: The instrument_format of this ExoticInstrument.  # noqa: E501
        :type: InstrumentDefinitionFormat
        """
        if instrument_format is None:
            raise ValueError("Invalid value for `instrument_format`, must not be `None`")  # noqa: E501

        self._instrument_format = instrument_format

    @property
    def content(self):
        """Gets the content of this ExoticInstrument.  # noqa: E501

        The original document received into the system. This format could potentially be anything though is most likely to be either Json or Xml. In the case where no other              interface is supported it is possible to fall back onto this.              For example, a trade from an external client system. This may be recognized internally by Lusid or simply passed through to another vendor system.  # noqa: E501

        :return: The content of this ExoticInstrument.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ExoticInstrument.

        The original document received into the system. This format could potentially be anything though is most likely to be either Json or Xml. In the case where no other              interface is supported it is possible to fall back onto this.              For example, a trade from an external client system. This may be recognized internally by Lusid or simply passed through to another vendor system.  # noqa: E501

        :param content: The content of this ExoticInstrument.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def instrument_type(self):
        """Gets the instrument_type of this ExoticInstrument.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit  # noqa: E501

        :return: The instrument_type of this ExoticInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this ExoticInstrument.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit  # noqa: E501

        :param instrument_type: The instrument_type of this ExoticInstrument.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashflowLeg", "Unknown", "TermDeposit"]  # noqa: E501
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
        if not isinstance(other, ExoticInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
