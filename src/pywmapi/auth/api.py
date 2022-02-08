import requests
from typing import Optional, Tuple
from enum import Enum
from bs4 import BeautifulSoup

from ..common import *
from .models import *


__all__ = [
    "get_csrf_and_jwt",
    "SigninAuthtype",
    "signin",
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


class SigninAuthtype(Enum):
    cookie = "cookie"
    header = "header"


def signin(
    email: str,
    password: str,
    device_id: Optional[str] = None,
    auth_type: Optional[SigninAuthtype] = SigninAuthtype.cookie,
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
            "auth_type": auth_type.value if auth_type is not None else None,
        },
        headers={"x-csrftoken": csrf_token},
        cookies={"JWT": jwt},
    )
    res.raise_for_status()
    user = User.from_dict(res.json()["payload"]["user"])
    return Session(jwt, user)
