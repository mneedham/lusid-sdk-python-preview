# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3009
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CompleteRelationship(object):
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
        'href': 'str',
        'version': 'Version',
        'relationship_definition_id': 'ResourceId',
        'source_entity': 'RelatedEntity',
        'target_entity': 'RelatedEntity',
        'outward_description': 'str',
        'inward_description': 'str',
        'effective_from': 'datetime'
    }

    attribute_map = {
        'href': 'href',
        'version': 'version',
        'relationship_definition_id': 'relationshipDefinitionId',
        'source_entity': 'sourceEntity',
        'target_entity': 'targetEntity',
        'outward_description': 'outwardDescription',
        'inward_description': 'inwardDescription',
        'effective_from': 'effectiveFrom'
    }

    required_map = {
        'href': 'optional',
        'version': 'optional',
        'relationship_definition_id': 'required',
        'source_entity': 'required',
        'target_entity': 'required',
        'outward_description': 'required',
        'inward_description': 'required',
        'effective_from': 'optional'
    }

    def __init__(self, href=None, version=None, relationship_definition_id=None, source_entity=None, target_entity=None, outward_description=None, inward_description=None, effective_from=None):  # noqa: E501
        """
        CompleteRelationship - a model defined in OpenAPI

        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param version: 
        :type version: lusid.Version
        :param relationship_definition_id:  (required)
        :type relationship_definition_id: lusid.ResourceId
        :param source_entity:  (required)
        :type source_entity: lusid.RelatedEntity
        :param target_entity:  (required)
        :type target_entity: lusid.RelatedEntity
        :param outward_description:  Description of the relationship based on relationship definition's outward description. (required)
        :type outward_description: str
        :param inward_description:  Description of the relationship based on relationship definition's inward description. (required)
        :type inward_description: str
        :param effective_from:  The effective datetime from which the relationship is valid.
        :type effective_from: datetime

        """  # noqa: E501

        self._href = None
        self._version = None
        self._relationship_definition_id = None
        self._source_entity = None
        self._target_entity = None
        self._outward_description = None
        self._inward_description = None
        self._effective_from = None
        self.discriminator = None

        self.href = href
        if version is not None:
            self.version = version
        self.relationship_definition_id = relationship_definition_id
        self.source_entity = source_entity
        self.target_entity = target_entity
        self.outward_description = outward_description
        self.inward_description = inward_description
        if effective_from is not None:
            self.effective_from = effective_from

    @property
    def href(self):
        """Gets the href of this CompleteRelationship.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this CompleteRelationship.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CompleteRelationship.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this CompleteRelationship.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def version(self):
        """Gets the version of this CompleteRelationship.  # noqa: E501


        :return: The version of this CompleteRelationship.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CompleteRelationship.


        :param version: The version of this CompleteRelationship.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def relationship_definition_id(self):
        """Gets the relationship_definition_id of this CompleteRelationship.  # noqa: E501


        :return: The relationship_definition_id of this CompleteRelationship.  # noqa: E501
        :rtype: ResourceId
        """
        return self._relationship_definition_id

    @relationship_definition_id.setter
    def relationship_definition_id(self, relationship_definition_id):
        """Sets the relationship_definition_id of this CompleteRelationship.


        :param relationship_definition_id: The relationship_definition_id of this CompleteRelationship.  # noqa: E501
        :type: ResourceId
        """
        if relationship_definition_id is None:
            raise ValueError("Invalid value for `relationship_definition_id`, must not be `None`")  # noqa: E501

        self._relationship_definition_id = relationship_definition_id

    @property
    def source_entity(self):
        """Gets the source_entity of this CompleteRelationship.  # noqa: E501


        :return: The source_entity of this CompleteRelationship.  # noqa: E501
        :rtype: RelatedEntity
        """
        return self._source_entity

    @source_entity.setter
    def source_entity(self, source_entity):
        """Sets the source_entity of this CompleteRelationship.


        :param source_entity: The source_entity of this CompleteRelationship.  # noqa: E501
        :type: RelatedEntity
        """
        if source_entity is None:
            raise ValueError("Invalid value for `source_entity`, must not be `None`")  # noqa: E501

        self._source_entity = source_entity

    @property
    def target_entity(self):
        """Gets the target_entity of this CompleteRelationship.  # noqa: E501


        :return: The target_entity of this CompleteRelationship.  # noqa: E501
        :rtype: RelatedEntity
        """
        return self._target_entity

    @target_entity.setter
    def target_entity(self, target_entity):
        """Sets the target_entity of this CompleteRelationship.


        :param target_entity: The target_entity of this CompleteRelationship.  # noqa: E501
        :type: RelatedEntity
        """
        if target_entity is None:
            raise ValueError("Invalid value for `target_entity`, must not be `None`")  # noqa: E501

        self._target_entity = target_entity

    @property
    def outward_description(self):
        """Gets the outward_description of this CompleteRelationship.  # noqa: E501

        Description of the relationship based on relationship definition's outward description.  # noqa: E501

        :return: The outward_description of this CompleteRelationship.  # noqa: E501
        :rtype: str
        """
        return self._outward_description

    @outward_description.setter
    def outward_description(self, outward_description):
        """Sets the outward_description of this CompleteRelationship.

        Description of the relationship based on relationship definition's outward description.  # noqa: E501

        :param outward_description: The outward_description of this CompleteRelationship.  # noqa: E501
        :type: str
        """
        if outward_description is None:
            raise ValueError("Invalid value for `outward_description`, must not be `None`")  # noqa: E501

        self._outward_description = outward_description

    @property
    def inward_description(self):
        """Gets the inward_description of this CompleteRelationship.  # noqa: E501

        Description of the relationship based on relationship definition's inward description.  # noqa: E501

        :return: The inward_description of this CompleteRelationship.  # noqa: E501
        :rtype: str
        """
        return self._inward_description

    @inward_description.setter
    def inward_description(self, inward_description):
        """Sets the inward_description of this CompleteRelationship.

        Description of the relationship based on relationship definition's inward description.  # noqa: E501

        :param inward_description: The inward_description of this CompleteRelationship.  # noqa: E501
        :type: str
        """
        if inward_description is None:
            raise ValueError("Invalid value for `inward_description`, must not be `None`")  # noqa: E501

        self._inward_description = inward_description

    @property
    def effective_from(self):
        """Gets the effective_from of this CompleteRelationship.  # noqa: E501

        The effective datetime from which the relationship is valid.  # noqa: E501

        :return: The effective_from of this CompleteRelationship.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this CompleteRelationship.

        The effective datetime from which the relationship is valid.  # noqa: E501

        :param effective_from: The effective_from of this CompleteRelationship.  # noqa: E501
        :type: datetime
        """

        self._effective_from = effective_from

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
        if not isinstance(other, CompleteRelationship):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
