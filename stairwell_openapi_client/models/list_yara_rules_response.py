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
from stairwell_openapi_client.models.yara_rule import YaraRule

class ListYaraRulesResponse(BaseModel):
    """
    ListYaraRulesResponse contains a list of rules and the next page token.  # noqa: E501
    """
    yara_rules: Optional[conlist(YaraRule)] = Field(default=None, alias="yaraRules", description="The rules from the parent resource.")
    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken", description="A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["yaraRules", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> ListYaraRulesResponse:
        """Create an instance of ListYaraRulesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in yara_rules (list)
        _items = []
        if self.yara_rules:
            for _item in self.yara_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['yaraRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListYaraRulesResponse:
        """Create an instance of ListYaraRulesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListYaraRulesResponse.parse_obj(obj)

        _obj = ListYaraRulesResponse.parse_obj({
            "yara_rules": [YaraRule.from_dict(_item) for _item in obj.get("yaraRules")] if obj.get("yaraRules") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj


