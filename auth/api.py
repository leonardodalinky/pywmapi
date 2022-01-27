import requests
from typing import Optional, Tuple
from enum import Enum
from bs4 import BeautifulSoup

from common import *
from .models import *


def get_csrf_and_jwt() -> Tuple[str, str]:
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
) -> Session:
    csrf_token, jwt = get_csrf_and_jwt()
    res = requests.post(
        API_BASE_URL + "/auth/signin",
        json={
            "email": email,
            "password": password,
            "device_id": device_id,
            "auth_type": auth_type,
        },
        headers={"x-csrftoken": csrf_token},
        cookies={"JWT": jwt},
    )
    res.raise_for_status()
    user = User.from_dict(res.json()["payload"]["user"])
    return Session(jwt, user)
