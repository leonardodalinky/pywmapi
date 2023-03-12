from enum import Enum
from typing import Optional, Tuple

import requests
from bs4 import BeautifulSoup

from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "get_csrf_and_jwt",
    "SigninAuthtype",
    "signin",
    # "restore",
]


def get_csrf_and_jwt() -> Tuple[str, str]:
    """Get csrf token and jwt token

    Returns:
        Tuple[str, str]: csrf & jwt
    """
    # get csrf_token first
    res = requests.get(HOMEPAGE_URL)
    soup = BeautifulSoup(res.text, features="html.parser")
    csrf_token = soup.find("meta", attrs={"name": "csrf-token"})["content"]
    # then get jwt
    jwt = res.cookies["JWT"]
    return csrf_token, jwt


class SigninAuthtype(str, Enum):
    cookie = "cookie"
    header = "header"


def signin(
    email: str,
    password: str,
    device_id: Optional[str] = None,
    auth_type: Optional[SigninAuthtype] = SigninAuthtype.cookie,
    ws_platform: Platform = Platform.pc,
    ws_on_message: Optional[MessageCallback] = None,
) -> Session:
    """Login to the account

    Args:
        email (str): email address for signin
        password (str): password
        device_id (Optional[str], optional): used to identify different devices. Defaults to None.
        auth_type (Optional[SigninAuthtype], optional): type of authentication. Defaults to SigninAuthtype.cookie.

    Returns:
        Session: session for the login state
    """
    csrf_token, jwt = get_csrf_and_jwt()
    res = requests.post(
        API_BASE_URL + "/auth/signin",
        json={
            "email": email,
            "password": password,
            "device_id": device_id,
            "auth_type": auth_type.value,
        },
        headers={"X-CSRFToken": csrf_token},
        cookies={"JWT": jwt},
    )
    check_wm_response(res)
    user = User.from_dict(res.json()["payload"]["user"])
    return Session(res.cookies["JWT"], csrf_token, user, ws_platform, on_message=ws_on_message)


def restore(email: str) -> None:
    """(CAUTION)Recieve mail with the new password, short after api call

    Args:
        email (str): email address

    Warnings:
        This function is unavailable since ReCaptcha is in the way.
    """
    raise NotImplementedError("ReCaptcha didn't work for now.")
    csrf_token, jwt = get_csrf_and_jwt()
    res = requests.post(
        API_BASE_URL + "/auth/restore",
        json={
            "email": email,
        },
        headers={"x-csrftoken": csrf_token},
        cookies={"JWT": jwt},
    )
    check_wm_response(res)
