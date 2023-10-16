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
        name: str
        icon: str
        description: str
        exposed: bool
        # might be always `patreon`
        type: str

    id: str
    """User ID."""
    ingame_name: str
    """In-game name."""
    status: ProfileStatus
    """Wfm status."""
    platform: Platform
    region: str
    banned: bool
    avatar: str
    last_seen: datetime
    reputation: int
    about: str
    """User's about-me section. Rendered as HTML."""
    about_raw: str
    """User's about-me section. Raw text."""
    own_profile: bool
    achievements: List[Achievement]
    ban_reason: Optional[str] = None
    background: Optional[str] = None
