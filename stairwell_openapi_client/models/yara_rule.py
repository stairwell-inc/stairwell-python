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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from stairwell_openapi_client.models.tag import Tag

class YaraRule(BaseModel):
    """
    YaraRule contains metadata and definition of a particular rule.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description="The resource name of the rule.")
    definition: StrictStr = Field(default=..., description="Definition of the rule.")
    scan_warning: Optional[StrictStr] = Field(default=None, alias="scanWarning", description="Warning from a failed canary scan.")
    state: Optional[StrictStr] = Field(default=None, description="Current scan inclusion state of rule.")
    update_time: Optional[datetime] = Field(default=None, alias="updateTime", description="Timestamp at which the latest rule version was submitted.")
    canary_scan_state: Optional[StrictStr] = Field(default=None, alias="canaryScanState", description="State from running this rule against known goodware.")
    tags: Optional[conlist(Tag)] = Field(default=None, description="Tags associated with this yara rule.")
    __properties = ["name", "definition", "scanWarning", "state", "updateTime", "canaryScanState", "tags"]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('STATE_UNSPECIFIED', 'STATE_INACTIVE', 'STATE_ACTIVE', 'STATE_ANCESTOR', 'STATE_DELETED'):
            raise ValueError("must be one of enum values ('STATE_UNSPECIFIED', 'STATE_INACTIVE', 'STATE_ACTIVE', 'STATE_ANCESTOR', 'STATE_DELETED')")
        return value

    @validator('canary_scan_state')
    def canary_scan_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CANARY_SCAN_STATE_UNSPECIFIED', 'PASSED_CANARY', 'FAILED_CANARY_UNKNOWN', 'FAILED_CANARY_MATCHES', 'FAILED_CANARY_SLOW_SCAN', 'FAILED_CANARY_COMPILER_WARNINGS', 'FAILED_CANARY_SCAN_ERROR'):
            raise ValueError("must be one of enum values ('CANARY_SCAN_STATE_UNSPECIFIED', 'PASSED_CANARY', 'FAILED_CANARY_UNKNOWN', 'FAILED_CANARY_MATCHES', 'FAILED_CANARY_SLOW_SCAN', 'FAILED_CANARY_COMPILER_WARNINGS', 'FAILED_CANARY_SCAN_ERROR')")
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
    def from_json(cls, json_str: str) -> YaraRule:
        """Create an instance of YaraRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "scan_warning",
                            "state",
                            "update_time",
                            "canary_scan_state",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> YaraRule:
        """Create an instance of YaraRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return YaraRule.parse_obj(obj)

        _obj = YaraRule.parse_obj({
            "name": obj.get("name"),
            "definition": obj.get("definition"),
            "scan_warning": obj.get("scanWarning"),
            "state": obj.get("state"),
            "update_time": obj.get("updateTime"),
            "canary_scan_state": obj.get("canaryScanState"),
            "tags": [Tag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None
        })
        return _obj


