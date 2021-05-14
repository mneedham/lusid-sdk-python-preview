# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3015
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CdsProtectionDetailSpecification(object):
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
        'seniority': 'str',
        'restructuring_type': 'str',
        'protect_start_day': 'bool',
        'pay_accrued_interest_on_default': 'bool'
    }

    attribute_map = {
        'seniority': 'seniority',
        'restructuring_type': 'restructuringType',
        'protect_start_day': 'protectStartDay',
        'pay_accrued_interest_on_default': 'payAccruedInterestOnDefault'
    }

    required_map = {
        'seniority': 'required',
        'restructuring_type': 'required',
        'protect_start_day': 'required',
        'pay_accrued_interest_on_default': 'required'
    }

    def __init__(self, seniority=None, restructuring_type=None, protect_start_day=None, pay_accrued_interest_on_default=None):  # noqa: E501
        """
        CdsProtectionDetailSpecification - a model defined in OpenAPI

        :param seniority:  The available values are: Unknown, SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2 (required)
        :type seniority: str
        :param restructuring_type:  The available values are: Unknown, CR, MR, MM, XR (required)
        :type restructuring_type: str
        :param protect_start_day:  Does the protection leg pay out in the case of default on the start date (required)
        :type protect_start_day: bool
        :param pay_accrued_interest_on_default:  Should accrued interest on the premium leg be paid if a credit event occurs (required)
        :type pay_accrued_interest_on_default: bool

        """  # noqa: E501

        self._seniority = None
        self._restructuring_type = None
        self._protect_start_day = None
        self._pay_accrued_interest_on_default = None
        self.discriminator = None

        self.seniority = seniority
        self.restructuring_type = restructuring_type
        self.protect_start_day = protect_start_day
        self.pay_accrued_interest_on_default = pay_accrued_interest_on_default

    @property
    def seniority(self):
        """Gets the seniority of this CdsProtectionDetailSpecification.  # noqa: E501

        The available values are: Unknown, SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2  # noqa: E501

        :return: The seniority of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: str
        """
        return self._seniority

    @seniority.setter
    def seniority(self, seniority):
        """Sets the seniority of this CdsProtectionDetailSpecification.

        The available values are: Unknown, SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2  # noqa: E501

        :param seniority: The seniority of this CdsProtectionDetailSpecification.  # noqa: E501
        :type: str
        """
        if seniority is None:
            raise ValueError("Invalid value for `seniority`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "SNR", "SUB", "JRSUBUT2", "PREFT1", "SECDOM", "SNRFOR", "SUBLT2"]  # noqa: E501
        if seniority not in allowed_values:
            raise ValueError(
                "Invalid value for `seniority` ({0}), must be one of {1}"  # noqa: E501
                .format(seniority, allowed_values)
            )

        self._seniority = seniority

    @property
    def restructuring_type(self):
        """Gets the restructuring_type of this CdsProtectionDetailSpecification.  # noqa: E501

        The available values are: Unknown, CR, MR, MM, XR  # noqa: E501

        :return: The restructuring_type of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: str
        """
        return self._restructuring_type

    @restructuring_type.setter
    def restructuring_type(self, restructuring_type):
        """Sets the restructuring_type of this CdsProtectionDetailSpecification.

        The available values are: Unknown, CR, MR, MM, XR  # noqa: E501

        :param restructuring_type: The restructuring_type of this CdsProtectionDetailSpecification.  # noqa: E501
        :type: str
        """
        if restructuring_type is None:
            raise ValueError("Invalid value for `restructuring_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "CR", "MR", "MM", "XR"]  # noqa: E501
        if restructuring_type not in allowed_values:
            raise ValueError(
                "Invalid value for `restructuring_type` ({0}), must be one of {1}"  # noqa: E501
                .format(restructuring_type, allowed_values)
            )

        self._restructuring_type = restructuring_type

    @property
    def protect_start_day(self):
        """Gets the protect_start_day of this CdsProtectionDetailSpecification.  # noqa: E501

        Does the protection leg pay out in the case of default on the start date  # noqa: E501

        :return: The protect_start_day of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._protect_start_day

    @protect_start_day.setter
    def protect_start_day(self, protect_start_day):
        """Sets the protect_start_day of this CdsProtectionDetailSpecification.

        Does the protection leg pay out in the case of default on the start date  # noqa: E501

        :param protect_start_day: The protect_start_day of this CdsProtectionDetailSpecification.  # noqa: E501
        :type: bool
        """
        if protect_start_day is None:
            raise ValueError("Invalid value for `protect_start_day`, must not be `None`")  # noqa: E501

        self._protect_start_day = protect_start_day

    @property
    def pay_accrued_interest_on_default(self):
        """Gets the pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.  # noqa: E501

        Should accrued interest on the premium leg be paid if a credit event occurs  # noqa: E501

        :return: The pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._pay_accrued_interest_on_default

    @pay_accrued_interest_on_default.setter
    def pay_accrued_interest_on_default(self, pay_accrued_interest_on_default):
        """Sets the pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.

        Should accrued interest on the premium leg be paid if a credit event occurs  # noqa: E501

        :param pay_accrued_interest_on_default: The pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.  # noqa: E501
        :type: bool
        """
        if pay_accrued_interest_on_default is None:
            raise ValueError("Invalid value for `pay_accrued_interest_on_default`, must not be `None`")  # noqa: E501

        self._pay_accrued_interest_on_default = pay_accrued_interest_on_default

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
        if not isinstance(other, CdsProtectionDetailSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
