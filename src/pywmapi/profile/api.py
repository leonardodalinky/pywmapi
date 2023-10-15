import requests

from ..auth import Session, User
from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "get_current_user",
    "get_profile_by_username",
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
        API_BASE_URL + f"/profile",
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
        API_BASE_URL + f"/profile/{username}",
    )
    check_wm_response(res)
    return Profile.from_dict(res.json()["payload"]["profile"])


def set_profile_status(sess: Session, status: ProfileStatus) -> None:
    """Switch the profile status

    Args:
        sess (Session): session
        status (ProfileStatus): online/offline/ingame
    """
    sess.send_msg(WSMessage[str](WSType.SET_STATUS, status))
