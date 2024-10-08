# coding: utf-8

"""
    Stairwell V1 HTTP APIs

    Restful APIs for the Stairwell platform. Most APIs expose named resources: each resource has a unique identifier that users use to reference that resource, and these names are what users should store as the canonical names for the resources. The base URL for this API is https://app.stairwell.com

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from stairwell_openapi_client.models.dns_lookup_result import DNSLookupResult

class HostnameMetadata(BaseModel):
    """
    HostnameMetadata contains metadata relating to a hostname.  # noqa: E501
    """
    name: StrictStr = Field(default=..., description="The resource name of the hostname.")
    hostname: StrictStr = Field(default=..., description="Hostname examples are - hurirk.net - www.tcoolonline.mobi - www.crackedmindstechnologies.com")
    a_records: Optional[conlist(DNSLookupResult)] = Field(default=None, alias="aRecords", description="A records (IPv4).")
    aaaa_records: Optional[conlist(DNSLookupResult)] = Field(default=None, alias="aaaaRecords", description="AAAA records (IPv6).")
    mx_records: Optional[conlist(DNSLookupResult)] = Field(default=None, alias="mxRecords", description="MX records.")
    __properties = ["name", "hostname", "aRecords", "aaaaRecords", "mxRecords"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HostnameMetadata:
        """Create an instance of HostnameMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in a_records (list)
        _items = []
        if self.a_records:
            for _item in self.a_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in aaaa_records (list)
        _items = []
        if self.aaaa_records:
            for _item in self.aaaa_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aaaaRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mx_records (list)
        _items = []
        if self.mx_records:
            for _item in self.mx_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mxRecords'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HostnameMetadata:
        """Create an instance of HostnameMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostnameMetadata.parse_obj(obj)

        _obj = HostnameMetadata.parse_obj({
            "name": obj.get("name"),
            "hostname": obj.get("hostname"),
            "a_records": [DNSLookupResult.from_dict(_item) for _item in obj.get("aRecords")] if obj.get("aRecords") is not None else None,
            "aaaa_records": [DNSLookupResult.from_dict(_item) for _item in obj.get("aaaaRecords")] if obj.get("aaaaRecords") is not None else None,
            "mx_records": [DNSLookupResult.from_dict(_item) for _item in obj.get("mxRecords")] if obj.get("mxRecords") is not None else None
        })
        return _obj


