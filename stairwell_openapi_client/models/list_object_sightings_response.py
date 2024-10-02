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
from stairwell_openapi_client.models.object_sighting import ObjectSighting

class ListObjectSightingsResponse(BaseModel):
    """
    Response type for ListObjectSightings RPCs.  # noqa: E501
    """
    object_sightings: Optional[conlist(ObjectSighting)] = Field(default=None, alias="objectSightings", description="The sightings from the parent resource.")
    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken", description="A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["objectSightings", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> ListObjectSightingsResponse:
        """Create an instance of ListObjectSightingsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in object_sightings (list)
        _items = []
        if self.object_sightings:
            for _item in self.object_sightings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['objectSightings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListObjectSightingsResponse:
        """Create an instance of ListObjectSightingsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListObjectSightingsResponse.parse_obj(obj)

        _obj = ListObjectSightingsResponse.parse_obj({
            "object_sightings": [ObjectSighting.from_dict(_item) for _item in obj.get("objectSightings")] if obj.get("objectSightings") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj


