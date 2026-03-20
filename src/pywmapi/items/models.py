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
    slug: str
    thumb: str
    item_slug: str

    @classmethod
    def from_dict(cls, data: dict) -> "ItemShort":
        return cls(
            id=data["id"],
            slug=data["slug"],
            thumb=data["i18n"]["en"]["thumb"],
            item_slug=data["i18n"]["en"]["name"],
        )


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
    slug: str
    """Item URL slug."""
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
    vaulted: Optional[bool] = None
    """Vaulted status of a relic. Only for relics."""
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

    @classmethod
    def from_dict(cls, data: dict) -> "ItemShort":
        return cls(
            id=data.get("id"),
            slug=data.get("slug"),
            icon=data["i18n"]["en"].get("icon"),
            thumb=data["i18n"]["en"].get("thumb"),
            tags=data.get("tags"),
            trading_tax=data.get("tradingTax"),
            sub_icon=data["i18n"]["en"].get("subIcon"),
            quantity_for_set=data.get("quantityInSet"),
            mod_max_rank=data.get("maxRank"),
            subtypes=data.get("subtypes"),
            cyan_stars=data.get("cyanStars"),
            amber_stars=data.get("amberStars"),
            vaulted=data.get("vaulted"),
            ducats=data.get("ducats"),
            set_root=data.get("setRoot"),
            mastery_level=data.get("reqMasteryRank"),
            rarity=cls.Rarity(data["rarity"]) if "rarity" in data else None,
        )
