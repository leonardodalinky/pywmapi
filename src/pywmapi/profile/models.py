from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from dacite import Config

from ..common import *

__all__ = [
    "ProfileStatus",
    "Profile",
]


@dataclass
class Profile(ModelBase):
    @dataclass
    class Achievement:
        name: str
        icon: str
        description: str
        exposed: bool
        # might be always `patreon`
        type: str

    id: str
    ingame_name: str
    status: ProfileStatus
    platform: Platform
    region: str
    banned: bool
    ban_reason: Optional[str]
    avatar: str
    background: Optional[str]
    last_seen: datetime
    reputation: int
    # HTML-rendered
    about: str
    # raw
    about_raw: str
    own_profile: bool
    achievements: List[Achievement]
