# coding: utf-8

"""
    playground

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class RunProcessParams(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cmd: StrictStr = ...
    env_vars: Optional[Dict[str, StrictStr]] = Field(None, alias="envVars")
    rootdir: Optional[StrictStr] = None
    __properties = ["cmd", "envVars", "rootdir"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RunProcessParams:
        """Create an instance of RunProcessParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RunProcessParams:
        """Create an instance of RunProcessParams from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RunProcessParams.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in RunProcessParams) in the input: " + obj)

        _obj = RunProcessParams.parse_obj({
            "cmd": obj.get("cmd"),
            "env_vars": obj.get("envVars"),
            "rootdir": obj.get("rootdir")
        })
        return _obj
