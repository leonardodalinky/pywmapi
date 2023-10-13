from typing import List

import requests

from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "list_items",
    "list_attrs",
]


def list_items(lang: Language = Language.en) -> List[RivenItem]:
    """List all riven templates

    Args:
        lang (Optional[Language], optional): addition language support. Defaults to Language.en.

    Returns:
        List[RivenItem]: items
    """
    res = requests.get(
        API_BASE_URL + "/riven/items",
        headers={"Language": lang.value},
    )
    check_wm_response(res)
    return list(map(lambda x: RivenItem.from_dict(x), res.json()["payload"]["items"]))


def list_attrs(lang: Language = Language.en) -> List[RivenAttribute]:
    """List all riven attributes

    Args:
        lang (Optional[Language], optional): addition language support. Defaults to Language.en.

    Returns:
        List[RivenAttribute]: attributes
    """
    res = requests.get(
        API_BASE_URL + "/riven/attributes",
        headers={"Language": lang.value},
    )
    check_wm_response(res)
    return list(map(lambda x: RivenAttribute.from_dict(x), res.json()["payload"]["attributes"]))
