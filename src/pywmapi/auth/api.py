from enum import Enum
from typing import Optional

import requests

from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "get_jwt_token",
    "SigninAuthtype",
    "signin",
    # "restore",
]


def get_jwt_token() -> str:
    """Get jwt token

    Returns:
        str: jwt
    """
    # get csrf_token first
    res = requests.get(API_BASE_URL)
    return res.cookies["JWT"]


class SigninAuthtype(str, Enum):
    cookie = "cookie"
    header = "header"


def signin(
    email: str,
    password: str,
    device_id: Optional[str] = None,
    auth_type: SigninAuthtype = SigninAuthtype.header,
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
    jwt = get_jwt_token()
    res = requests.post(
        API_BASE_URL + "/auth/signin",
        json={
            "email": email,
            "password": password,
            "device_id": device_id,
            "auth_type": auth_type.value,
        },
        headers={"Authorization": jwt},
    )
    check_wm_response(res)
    data = res.json()["payload"]["user"]
    user = User.from_dict(data)
    return Session(res.headers["Authorization"], user, ws_platform, on_message=ws_on_message)


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
