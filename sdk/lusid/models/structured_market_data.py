# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2829
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class StructuredMarketData(object):
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
        'document_format': 'str',
        'version': 'str',
        'name': 'str',
        'document': 'str'
    }

    attribute_map = {
        'document_format': 'documentFormat',
        'version': 'version',
        'name': 'name',
        'document': 'document'
    }

    required_map = {
        'document_format': 'required',
        'version': 'optional',
        'name': 'optional',
        'document': 'required'
    }

    def __init__(self, document_format=None, version=None, name=None, document=None):  # noqa: E501
        """
        StructuredMarketData - a model defined in OpenAPI

        :param document_format:  The format of the accompanying document. (required)
        :type document_format: str
        :param version:  The semantic version of the document format; MAJOR.MINOR.PATCH
        :type version: str
        :param name:  The name or description for the document
        :type name: str
        :param document:  The document that will be stored (or retrieved) and which describes a structured market data entity such as a credit or interest rate curve (required)
        :type document: str

        """  # noqa: E501

        self._document_format = None
        self._version = None
        self._name = None
        self._document = None
        self.discriminator = None

        self.document_format = document_format
        self.version = version
        self.name = name
        self.document = document

    @property
    def document_format(self):
        """Gets the document_format of this StructuredMarketData.  # noqa: E501

        The format of the accompanying document.  # noqa: E501

        :return: The document_format of this StructuredMarketData.  # noqa: E501
        :rtype: str
        """
        return self._document_format

    @document_format.setter
    def document_format(self, document_format):
        """Sets the document_format of this StructuredMarketData.

        The format of the accompanying document.  # noqa: E501

        :param document_format: The document_format of this StructuredMarketData.  # noqa: E501
        :type: str
        """
        if document_format is None:
            raise ValueError("Invalid value for `document_format`, must not be `None`")  # noqa: E501

        self._document_format = document_format

    @property
    def version(self):
        """Gets the version of this StructuredMarketData.  # noqa: E501

        The semantic version of the document format; MAJOR.MINOR.PATCH  # noqa: E501

        :return: The version of this StructuredMarketData.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StructuredMarketData.

        The semantic version of the document format; MAJOR.MINOR.PATCH  # noqa: E501

        :param version: The version of this StructuredMarketData.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this StructuredMarketData.  # noqa: E501

        The name or description for the document  # noqa: E501

        :return: The name of this StructuredMarketData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StructuredMarketData.

        The name or description for the document  # noqa: E501

        :param name: The name of this StructuredMarketData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def document(self):
        """Gets the document of this StructuredMarketData.  # noqa: E501

        The document that will be stored (or retrieved) and which describes a structured market data entity such as a credit or interest rate curve  # noqa: E501

        :return: The document of this StructuredMarketData.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this StructuredMarketData.

        The document that will be stored (or retrieved) and which describes a structured market data entity such as a credit or interest rate curve  # noqa: E501

        :param document: The document of this StructuredMarketData.  # noqa: E501
        :type: str
        """
        if document is None:
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

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
        if not isinstance(other, StructuredMarketData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
