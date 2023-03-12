from typing import Dict, List, Optional, Tuple, Union

import requests

from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "list_weapons",
    "list_ephemeras",
    "list_quirks",
]


def list_weapons(lang: Optional[Language] = Language.en) -> List[LichWeapon]:
    """List all lich weapons

    Args:
        lang (Optional[Language], optional): addition language support. Defaults to Language.en.

    Returns:
        List[LichWeapon]: weapons
    """
    res = requests.get(
        API_BASE_URL + "/lich/weapons",
        headers={"Language": lang.value},
    )
    check_wm_response(res)
    return list(map(lambda x: LichWeapon.from_dict(x), res.json()["payload"]["weapons"]))


def list_ephemeras(lang: Optional[Language] = Language.en) -> List[LichEphemera]:
    """List all lich ephemeras

    Args:
        lang (Optional[Language], optional): addition language support. Defaults to Language.en.

    Returns:
        List[LichEphemera]: ephemeras
    """
    res = requests.get(
        API_BASE_URL + "/lich/ephemeras",
        headers={"Language": lang.value},
    )
    check_wm_response(res)
    return list(map(lambda x: LichEphemera.from_dict(x), res.json()["payload"]["ephemeras"]))


def list_quirks(lang: Optional[Language] = Language.en) -> List[LichQuirk]:
    """List all lich quirks

    Args:
        lang (Optional[Language], optional): addition language support. Defaults to Language.en.

    Returns:
        List[LichQuirk]: quirks
    """
    res = requests.get(
        API_BASE_URL + "/lich/quirks",
        headers={"Language": lang.value},
    )
    check_wm_response(res)
    return list(map(lambda x: LichQuirk.from_dict(x), res.json()["payload"]["quirks"]))
