from enum import Enum
from typing import List, Optional

from attrs import define

from ..common import *

__all__ = [
    "RivenItem",
    "RivenAttribute",
]


@define
class RivenItem(ModelBase):
    class Group(Enum):
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
    thumb: str
    item_name: str
    icon_format: Optional[IconFormat] = None


@define
class RivenAttribute(ModelBase):
    class Group(Enum):
        default = "default"
        melee = "melee"
        top = "top"

    class Units(Enum):
        percent = "percent"
        seconds = "seconds"
        # Not know what this is
        multiply = "multiply"

    id: str
    url_name: str
    group: Group
    positive_is_negative: bool
    effect: str
    negative_only: bool
    search_only: bool
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    exclusive_to: Optional[List[WeaponType]] = None
    units: Optional[Units] = None
