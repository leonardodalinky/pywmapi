from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from dacite import Config

from ..common import *

__all__ = [
    "LichWeapon",
    "LichEphemera",
    "LichQuirk",
]


@dataclass
class LichWeapon(ModelBase):
    id: str
    url_name: str
    icon: str
    icon_format: IconFormat
    thumb: str
    item_name: str


@dataclass
class LichEphemera(ModelBase):
    id: str
    url_name: str
    icon: str
    icon_format: IconFormat
    thumb: str
    animation: str
    animation_format: IconFormat
    element: ElementType
    item_name: str


@dataclass
class LichQuirk(ModelBase):
    id: str
    url_name: str
    item_name: str
    description: str
    group: str
