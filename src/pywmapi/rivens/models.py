from ctypes import cast
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from dacite import Config

from ..common import *

__all__ = [
    "RivenItem",
    "RivenAttribute",
]


@dataclass
class RivenItem(ModelBase):
    class Group(str, Enum):
        primary = "primary"
        secondary = "secondary"
        melee = "melee"
        zaw = "zaw"
        sentinel = "sentinel"
        archgun = "archgun"
        kitgun = "kitgun"

    id: str
    url_name: str
    group: Group
    riven_type: WeaponType
    icon: str
    icon_format: Optional[IconFormat]
    thumb: str
    item_name: str


@dataclass
class RivenAttribute(ModelBase):
    class Group(str, Enum):
        default = "default"
        melee = "melee"
        top = "top"

    class Units(str, Enum):
        percent = "percent"
        seconds = "seconds"

    id: str
    url_name: str
    group: Group
    prefix: Optional[str]
    suffix: Optional[str]
    positive_is_negative: bool
    exclusive_to: Optional[List[WeaponType]]
    effect: str
    units: Optional[Units]
    negative_only: bool
    search_only: bool
