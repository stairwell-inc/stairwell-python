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
from pydantic import BaseModel, Field, StrictStr, conlist
from stairwell_openapi_client.models.tag import Tag

class Asset(BaseModel):
    """
    Asset represents any entity (usually a machine) which uploads objects to the Stairwell platform.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description="The resource name of the asset.")
    label: Optional[StrictStr] = Field(default=None, description="Label of the asset.")
    create_time: Optional[datetime] = Field(default=None, alias="createTime", description="Creation time of the asset.")
    last_checkin_time: Optional[datetime] = Field(default=None, alias="lastCheckinTime", description="Last time the asset made an RPC into the platform.")
    environment: Optional[StrictStr] = Field(default=None, description="Environment that this asset lives in.")
    forwarder_version: Optional[StrictStr] = Field(default=None, alias="forwarderVersion", description="Forwarder version of the form {major}.{minor}.{patch}")
    mac_address: Optional[StrictStr] = Field(default=None, alias="macAddress", description="The media access control address specific to this asset.")
    os: Optional[StrictStr] = Field(default=None, description="Operating system running on this asset.")
    os_version: Optional[StrictStr] = Field(default=None, alias="osVersion", description="Operating system version of the form {major}.{minor}.{patch}")
    tags: Optional[conlist(Tag)] = Field(default=None, description="Tags associated with this asset.")
    upload_token: Optional[StrictStr] = Field(default=None, alias="uploadToken", description="Private authorization id and token for uploading to the asset")
    __properties = ["name", "label", "createTime", "lastCheckinTime", "environment", "forwarderVersion", "macAddress", "os", "osVersion", "tags", "uploadToken"]

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
    def from_json(cls, json_str: str) -> Asset:
        """Create an instance of Asset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "create_time",
                            "last_checkin_time",
                            "environment",
                            "forwarder_version",
                            "mac_address",
                            "os",
                            "os_version",
                            "tags",
                            "upload_token",
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
    def from_dict(cls, obj: dict) -> Asset:
        """Create an instance of Asset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Asset.parse_obj(obj)

        _obj = Asset.parse_obj({
            "name": obj.get("name"),
            "label": obj.get("label"),
            "create_time": obj.get("createTime"),
            "last_checkin_time": obj.get("lastCheckinTime"),
            "environment": obj.get("environment"),
            "forwarder_version": obj.get("forwarderVersion"),
            "mac_address": obj.get("macAddress"),
            "os": obj.get("os"),
            "os_version": obj.get("osVersion"),
            "tags": [Tag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "upload_token": obj.get("uploadToken")
        })
        return _obj


