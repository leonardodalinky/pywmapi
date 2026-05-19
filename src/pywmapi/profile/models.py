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
        name:str
        icon: str
        thumb: str
        description: str
        # might be always `patreon`
        type: str

    id: str
    """User ID."""
    slug: str
    status: ProfileStatus
    """Wfm status."""
    slug: str
    icon: str
    thumb: str
    platform: Platform
    locale: str
    banned: bool
    avatar: str
    lastSeen: datetime
    reputation: int
    about: str
    own_profile: bool
    achievementShowcase: Optional[List[Achievement]]
    banMessage: Optional[str] = None
    background: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict, achievementData: dict) -> "Profile":

        achievements = None

        if achievementData:
            achievements = []
            for item in achievementData:
                en_data = item.get("i18n").get("en")

                achievement = cls.Achievement(
                    id=item.get("id"),
                    type=item.get("type"),
                    name=en_data.get("name", "Unknown"),
                    description=en_data.get("description", ""),
                    icon=en_data.get("icon"),
                    thumb=en_data.get("thumb"),
                )
                
                achievements.append(achievement)

        return cls(
            id=data.get("id"),
            slug=data.get("slug"),
            status=ProfileStatus(data.get("status")),
            icon=data.get("icon"),
            thumb=data.get("thumb"),
            platform=Platform(data.get("platform")),
            locale=data.get("locale"),
            banned=data.get("banned", False),
            avatar=data.get("avatar"),
            lastSeen=datetime.fromisoformat(data.get("lastSeen").replace("Z", "+00:00")),
            reputation=data.get("reputation"),
            about=data.get("about"),
            own_profile=data.get("ownProfile", False),
            achievementShowcase=achievements,
            banMessage=data.get("banMessage"),
            background=data.get("background"),
        )
