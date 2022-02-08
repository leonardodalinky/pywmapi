from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, Any, Optional
from dacite import Config

from ..common import *


__all__ = [
    "Session",
    "UserShort",
    "User",
]


@dataclass
class Session:
    jwt: str
    user: "User"


@dataclass
class UserShort:
    class Status(Enum):
        ingame = "ingame"
        online = "online"
        offline = "offline"

    id: str
    ingame_name: str
    status: Status
    region: str
    reputation: int
    avatar: Optional[str]
    last_seen: datetime


@dataclass
class User(ModelBase):
    class Role(Enum):
        anonymous = "anonymous"
        user = "user"
        moderator = "moderator"
        admin = "admin"

    class PatreonBadge(Enum):
        bronze = "bronze"
        gold = "gold"
        silver = "silver"
        platinum = "platinum"

    @dataclass
    class PatreonProfile:
        patreon_founder: bool
        subscription: bool
        patreon_badge: str

    @dataclass
    class LinkedAccounts:
        steam_profile: bool
        patreon_profile: bool
        xbox_profile: bool
        discord_profile: bool

    id: str
    anonymous: bool
    verification: bool
    check_code: str
    ingame_name: str
    check_code: str
    patreon_profile: Optional[PatreonProfile]
    platform: Platform
    region: str
    banned: bool
    ban_reason: Optional[str]
    role: Role
    avatar: str
    background: Optional[str]
    linked_accounts: LinkedAccounts
    # `has_mail` is spelled as `has_email` mistakenly in the official api docs
    has_mail: bool
    written_reviews: int
    unread_messages: int
