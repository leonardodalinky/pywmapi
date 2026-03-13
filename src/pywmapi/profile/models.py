from datetime import datetime
from typing import List, Optional

from attrs import define, field

from ..common import *

__all__ = [
    "ProfileStatus",
    "Profile",
]


@define
class Profile(ModelBase):
    @define
    class Achievement:
        id: str
        icon: str
        description: str
        # might be always `patreon`
        type: str

    id: str
    """User ID."""
    slug: str
    status: ProfileStatus
    """Wfm status."""
    slug: str
    platform: Platform
    locale: str
    banned: bool
    avatar: str
    lastSeen: datetime
    reputation: int
    about: str
    own_profile: bool
    achievementShowcase: Optional[Achievement]
    banMessage: Optional[str] = None
    background: Optional[str] = None

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
