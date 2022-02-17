from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from dacite import Config

from ..common import *
from ..lang.models import LangInItem

__all__ = [
    "ItemShort",
    "ItemFull",
]


@dataclass
class ItemShort(ModelBase):
    id: str
    url_name: str
    thumb: str
    item_name: str


@dataclass
class ItemFull(ModelBase):
    class Rarity(str, Enum):
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
