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



from pydantic import BaseModel, Field, StrictStr

class TriggerObjectDetonationRequest(BaseModel):
    """
    Request for the TriggerObjectDetonationRequest RPC.  # noqa: E501
    """
    parent: StrictStr = Field(default=..., description="The parent resource where this detonation will be triggered.")
    __properties = ["parent"]

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
    def from_json(cls, json_str: str) -> TriggerObjectDetonationRequest:
        """Create an instance of TriggerObjectDetonationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TriggerObjectDetonationRequest:
        """Create an instance of TriggerObjectDetonationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TriggerObjectDetonationRequest.parse_obj(obj)

        _obj = TriggerObjectDetonationRequest.parse_obj({
            "parent": obj.get("parent")
        })
        return _obj


