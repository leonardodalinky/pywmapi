from typing import Optional

from attrs import define

from ..common import *

__all__ = [
    "LichWeapon",
    "LichEphemera",
    "LichQuirk",
]


@define
class LichWeapon(ModelBase):
    id: str
    url_name: str
    icon: str
    thumb: str
    item_name: str
    icon_format: Optional[IconFormat] = None


@define
class LichEphemera(ModelBase):
    id: str
    url_name: str
    icon: str
    thumb: str
    animation: str
    animation_format: IconFormat
    element: ElementType
    item_name: str
    icon_format: Optional[IconFormat] = None


@define
class LichQuirk(ModelBase):
    id: str
    url_name: str
    item_name: str
    description: str
    group: str
