from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, Any, Optional, List
from dacite import Config

from ..common import *
from ..lang.models import LangInItem
from ..auth.models import UserShort


__all__ = [
    "ItemShort",
    "ItemFull",
    "OrderCommon",
    "OrderRow",
    # "OrderFull",
]


@dataclass
class ItemShort(ModelBase):
    id: str
    url_name: str
    thumb: str
    item_name: str


@dataclass
class ItemFull(ModelBase):
    @dataclass
    class Rarity(Enum):
        common = "common"
        uncommon = "uncommon"
        rare = "rare"
        legendary = "legendary"
        peculiar = "peculiar"

    id: str
    url_name: str
    icon: str
    thumb: str
    sub_icon: Optional[str]
    quantity_for_set: Optional[int]
    mod_max_rank: Optional[int]
    # only for relics and fishes
    subtypes: Optional[List[str]]
    tags: List[str]
    cyan_stars: Optional[int]
    amber_stars: Optional[int]
    ducats: Optional[int]
    set_root: Optional[bool]
    mastery_level: Optional[int]
    rarity: Optional[Rarity]
    trading_tax: int
    # language items
    en: Optional[LangInItem]
    ru: Optional[LangInItem]
    ko: Optional[LangInItem]
    de: Optional[LangInItem]
    fr: Optional[LangInItem]
    pt: Optional[LangInItem]
    zh_hant: Optional[LangInItem]
    zh_hans: Optional[LangInItem]
    es: Optional[LangInItem]
    it: Optional[LangInItem]
    pl: Optional[LangInItem]


@dataclass
class OrderCommon(ModelBase):
    id: str
    platinum: int
    quantity: int
    order_type: OrderType
    platform: Platform
    region: Optional[str]
    creation_date: datetime
    last_update: datetime
    visible: bool


@dataclass
class OrderRow(OrderCommon):
    user: UserShort


@dataclass
class OrderFull(OrderRow):
    # TODO
    def __init__(self):
        raise NotImplementedError()
