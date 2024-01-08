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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class DNSLookupResult(BaseModel):
    """
    This represents result of a DNS lookup.  # noqa: E501
    """
    state: Optional[StrictStr] = Field(None, description="DNS lookup state")
    address: Optional[StrictStr] = Field(None, description="Address the hostname resolved to at lookup time.")
    lookup_time: Optional[datetime] = Field(None, alias="lookupTime", description="Time is the time the lookup was made.")
    __properties = ["state", "address", "lookupTime"]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('STATE_UNSPECIFIED', 'NOERROR', 'ERROR', 'NXDOMAIN', 'REFUSED', 'SERVFAIL', 'TIMEOUT'):
            raise ValueError("must be one of enum values ('STATE_UNSPECIFIED', 'NOERROR', 'ERROR', 'NXDOMAIN', 'REFUSED', 'SERVFAIL', 'TIMEOUT')")
        return value

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
    def from_json(cls, json_str: str) -> DNSLookupResult:
        """Create an instance of DNSLookupResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "state",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DNSLookupResult:
        """Create an instance of DNSLookupResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DNSLookupResult.parse_obj(obj)

        _obj = DNSLookupResult.parse_obj({
            "state": obj.get("state"),
            "address": obj.get("address"),
            "lookup_time": obj.get("lookupTime")
        })
        return _obj


