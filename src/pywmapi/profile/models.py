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
    ingameName: str
    """In-game name."""
    status: ProfileStatus
    """Wfm status."""
    slug: str
    platform: Platform
    region: str
    banned: bool
    avatar: str
    lastSeen: datetime
    reputation: int
    about: str
    own_profile: bool
    achievementShowcase: Optional[Achievement]
    banMessage: Optional[str] = None
    background: Optional[str] = None