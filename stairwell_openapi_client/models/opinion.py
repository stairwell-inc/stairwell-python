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

class Opinion(BaseModel):
    """
    Opinion represents a key value pairing applied to particular entity. Only one of object, rule or asset may be specified.  # noqa: E501
    """
    verdict: StrictStr = Field(..., description="The opinion put on the entity.")
    environment: StrictStr = Field(..., description="Environment the opinion is set in")
    email: Optional[StrictStr] = Field(None, description="The email of the user who made the opinion.")
    create_time: Optional[datetime] = Field(None, alias="createTime", description="The time when the opinion was added.")
    __properties = ["verdict", "environment", "email", "createTime"]

    @validator('verdict')
    def verdict_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('OPINION_VERDICT_UNSPECIFIED', 'NO_OPINION', 'TRUSTED', 'GRAYWARE', 'MALICIOUS'):
            raise ValueError("must be one of enum values ('OPINION_VERDICT_UNSPECIFIED', 'NO_OPINION', 'TRUSTED', 'GRAYWARE', 'MALICIOUS')")
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
    def from_json(cls, json_str: str) -> Opinion:
        """Create an instance of Opinion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "email",
                            "create_time",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Opinion:
        """Create an instance of Opinion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Opinion.parse_obj(obj)

        _obj = Opinion.parse_obj({
            "verdict": obj.get("verdict"),
            "environment": obj.get("environment"),
            "email": obj.get("email"),
            "create_time": obj.get("createTime")
        })
        return _obj

