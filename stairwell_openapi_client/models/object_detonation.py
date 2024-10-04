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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from stairwell_openapi_client.models.detection import Detection
from stairwell_openapi_client.models.file_action import FileAction
from stairwell_openapi_client.models.mitre_attack_ttp import MitreAttackTTP
from stairwell_openapi_client.models.registry_key_action import RegistryKeyAction

class ObjectDetonation(BaseModel):
    """
    ObjectDetonation contains the status of the detonation analysis and if the analysis is complete, information collected while detonating the application.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description="The resource name of the detonation.")
    tags: Optional[conlist(StrictStr)] = Field(default=None, description="tags are tags extracted from Triage.")
    overview: Optional[StrictStr] = Field(default=None, description="overview contains the overview provided by triage. https://pkg.go.dev/github.com/hatching/triage@v1.0.0/types#OverviewReport")
    raw_triage_reports: Optional[Dict[str, StrictStr]] = Field(default=None, alias="rawTriageReports", description="raw triage reports correspond to each individual sandbox run of an object. https://pkg.go.dev/github.com/hatching/triage@v1.0.0/types#TriageReport")
    sample_id: Optional[StrictStr] = Field(default=None, alias="sampleId", description="sample_id is the sampleID returned by Triage identifying the detonation.")
    files: Optional[conlist(FileAction)] = Field(default=None, description="Files which were accessed during the detonation.")
    registry_keys: Optional[conlist(RegistryKeyAction)] = Field(default=None, alias="registryKeys", description="Registry keys which were read/written/deleted.")
    executed_commands: Optional[conlist(StrictStr)] = Field(default=None, alias="executedCommands", description="Commands which were executed during the detonation")
    mutexes: Optional[conlist(StrictStr)] = Field(default=None, description="Mutexes which were used during the detonation.")
    signatures: Optional[conlist(StrictStr)] = Field(default=None, description="Any malware signatures which are detected during detonation.")
    mitre_attack_ttps: Optional[conlist(MitreAttackTTP)] = Field(default=None, alias="mitreAttackTtps", description="Any mitre signatures which are detected during detonation. Mitre TTPs reference: https://attack.mitre.org/techniques/enterprise/")
    created_services: Optional[conlist(StrictStr)] = Field(default=None, alias="createdServices", description="List of created serviced during detonation.")
    started_services: Optional[conlist(StrictStr)] = Field(default=None, alias="startedServices", description="List of started services during detonation.")
    dropped_files: Optional[conlist(StrictStr)] = Field(default=None, alias="droppedFiles", description="Dropped child file hashes.")
    in_memory_files: Optional[conlist(StrictStr)] = Field(default=None, alias="inMemoryFiles", description="In-memory child file hashes.")
    detections: Optional[conlist(Detection)] = Field(default=None, description="Detections (malware family, yara, suricata...)")
    __properties = ["name", "tags", "overview", "rawTriageReports", "sampleId", "files", "registryKeys", "executedCommands", "mutexes", "signatures", "mitreAttackTtps", "createdServices", "startedServices", "droppedFiles", "inMemoryFiles", "detections"]

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
    def from_json(cls, json_str: str) -> ObjectDetonation:
        """Create an instance of ObjectDetonation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in registry_keys (list)
        _items = []
        if self.registry_keys:
            for _item in self.registry_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['registryKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mitre_attack_ttps (list)
        _items = []
        if self.mitre_attack_ttps:
            for _item in self.mitre_attack_ttps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mitreAttackTtps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in detections (list)
        _items = []
        if self.detections:
            for _item in self.detections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['detections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObjectDetonation:
        """Create an instance of ObjectDetonation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObjectDetonation.parse_obj(obj)

        _obj = ObjectDetonation.parse_obj({
            "name": obj.get("name"),
            "tags": obj.get("tags"),
            "overview": obj.get("overview"),
            "raw_triage_reports": obj.get("rawTriageReports"),
            "sample_id": obj.get("sampleId"),
            "files": [FileAction.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "registry_keys": [RegistryKeyAction.from_dict(_item) for _item in obj.get("registryKeys")] if obj.get("registryKeys") is not None else None,
            "executed_commands": obj.get("executedCommands"),
            "mutexes": obj.get("mutexes"),
            "signatures": obj.get("signatures"),
            "mitre_attack_ttps": [MitreAttackTTP.from_dict(_item) for _item in obj.get("mitreAttackTtps")] if obj.get("mitreAttackTtps") is not None else None,
            "created_services": obj.get("createdServices"),
            "started_services": obj.get("startedServices"),
            "dropped_files": obj.get("droppedFiles"),
            "in_memory_files": obj.get("inMemoryFiles"),
            "detections": [Detection.from_dict(_item) for _item in obj.get("detections")] if obj.get("detections") is not None else None
        })
        return _obj


