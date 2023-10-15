from typing import List, Tuple
from warnings import warn

import requests

from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "list_items",
    "get_item",
    "get_orders",
]


def list_items(lang: Language = Language.en) -> List[ItemShort]:
    """List all the tradable items in wm's databases

    Args:
        lang (Optional[Language], optional): addition language support. Defaults to Language.en.

    Returns:
        List[ItemShort]: items
    """
    res = requests.get(
        API_BASE_URL + "/items",
        headers={"Language": lang.value},
    )
    check_wm_response(res)
    return list(map(lambda x: ItemShort.from_dict(x), res.json()["payload"]["items"]))


def get_item(url_name: str, platform: Platform = Platform.pc) -> Tuple[ItemFull, List[ItemFull]]:
    """Get info of an item

    Args:
        url_name (str): unique name for an item
        platform (Optional[Platform], optional): platform. Defaults to Platform.pc.

    Returns:
        Tuple[ItemFull, List[ItemFull]]: the first is the target item; the second is the whole set of items containing the target item
    """
    res = requests.get(
        API_BASE_URL + f"/items/{url_name}",
        headers={"Platform": platform.value},
    )
    check_wm_response(res)
    item_json = res.json()["payload"]["item"]
    return _transform_item_result(item_json)


def get_orders(*args, **kwargs):
    """The same as `orders.get_orders`"""
    warn(
        "`get_orders` is moved to package `orders` in v1.1. This function would be deprecated in the future."
    )
    from ..orders.api import get_orders

    return get_orders(*args, **kwargs)


def _transform_item_result(item_json) -> Tuple[ItemFull, List[ItemFull]]:
    items_in_set = list(map(lambda x: ItemFull.from_dict(x), item_json["items_in_set"]))

    target_item = None
    for item in items_in_set:
        if item.id == item_json["id"]:
            target_item = item
            break
    if target_item is None:
        raise RuntimeError("could not find item")
    return target_item, items_in_set
