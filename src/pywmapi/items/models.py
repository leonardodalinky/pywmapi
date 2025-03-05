from enum import Enum
from typing import List, Optional

from attrs import define

from ..common import *
from ..lang.models import LangInItem

__all__ = [
    "ItemShort",
    "ItemFull",
]


@define
class ItemShort(ModelBase):
    id: str
    url_name: str
    thumb: str
    item_name: str


@define
class ItemFull(ModelBase):
    class Rarity(Enum):
        common = "common"
        uncommon = "uncommon"
        rare = "rare"
        legendary = "legendary"
        peculiar = "peculiar"
        archon = "archon"

    id: str
    """Item ID."""
    url_name: str
    """Item URL name."""
    icon: str
    thumb: str
    tags: List[str]
    trading_tax: int
    sub_icon: Optional[str] = None
    quantity_for_set: Optional[int] = None
    mod_max_rank: Optional[int] = None
    """Max rank for mods. Only for mods."""
    # only for relics and fishes
    subtypes: Optional[List[str]] = None
    cyan_stars: Optional[int] = None
    """Cyan stars count. Only for Ayatan Treasures."""
    amber_stars: Optional[int] = None
    """Amber stars count. Only for Ayatan Treasures."""
    ducats: Optional[int] = None
    set_root: Optional[bool] = None
    mastery_level: Optional[int] = None
    rarity: Optional[Rarity] = None
    # language items
    en: Optional[LangInItem] = None
    ru: Optional[LangInItem] = None
    ko: Optional[LangInItem] = None
    de: Optional[LangInItem] = None
    fr: Optional[LangInItem] = None
    pt: Optional[LangInItem] = None
    zh_hant: Optional[LangInItem] = None
    zh_hans: Optional[LangInItem] = None
    es: Optional[LangInItem] = None
    it: Optional[LangInItem] = None
    pl: Optional[LangInItem] = None
