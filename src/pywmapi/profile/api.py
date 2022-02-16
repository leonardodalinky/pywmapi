from typing import Dict, List, Optional, Tuple, Union

import requests

from ..auth import Session, User
from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "get_current_user",
    "get_profile_by_username",
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
        headers={"X-CSRFToken": sess.csrf_token},
        cookies={"JWT": sess.jwt},
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
