from typing import List

import requests

from ..auth import Session, User
from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "get_current_user",
    "get_profile_by_username",
    "get_profile_achievements",
    "set_profile_status",
]


def get_current_user(sess: Session) -> User:
    """Get current user

    Args:
        sess (Session): session

    Returns:
        User: user
    """
    res = requests.get(
        API_BASE_URL + f"/user",
        **sess.to_header_dict(),
    )
    check_wm_response(res)
    return User.from_dict(res.json()["profile"])


def get_profile_by_username(username: str) -> Profile:
    """Get user profile by username

    Args:
        username (str): username

    Returns:
        Profile: user profile
    """
    res = requests.get(
        API_BASE_URL + f"/user/{username}",
    )
    achievementRes = requests.get(API_BASE_URL + f"/achievements/user/{username}")
    check_wm_response(res)
    check_wm_response(achievementRes)
    return Profile.from_dict(res.json()["data"], achievementRes.json()["data"])


def get_profile_achievements(username: str) -> List[Profile.Achievement]:
    """Get achievements of a specific profile

    Args:
        username (str): username

    Returns:
        List[Achievement]: List of achievements held by user profile
    """
    return get_profile_by_username(username).achievementShowcase


def set_profile_status(sess: Session, status: ProfileStatus) -> None:
    """Switch the profile status

    Args:
        sess (Session): session
        status (ProfileStatus): online/offline/ingame
    """
    sess.send_msg(WSMessage[str](WSType.SET_STATUS, status))
