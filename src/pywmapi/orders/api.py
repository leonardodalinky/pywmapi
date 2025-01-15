from typing import List, Optional, Tuple, Union, overload

import requests
from attrs import asdict

from ..auth import Session
from ..common import *
from ..exceptions import *
from ..items.api import _transform_item_result
from ..items.models import *
from ..utils import *
from .models import *

__all__ = [
    "get_orders",
    "get_current_orders",
    "get_orders_by_username",
    # "get_individual_order",
    "add_order",
    "update_order",
    "delete_order",
]


@overload
def get_orders(url_name: str, platform: Platform = Platform.pc) -> List[OrderRow]: ...


@overload
def get_orders(
    url_name: str,
    platform: Platform = Platform.pc,
    include: IncludeOption = IncludeOption.item,
) -> Tuple[List[OrderRow], ItemFull, List[ItemFull]]: ...


def get_orders(
    url_name: str,
    platform: Platform = Platform.pc,
    include: Optional[IncludeOption] = None,
) -> Union[List[OrderRow], Tuple[List[OrderRow], ItemFull, List[ItemFull]]]:
    """Get orders of an item

    Args:
        url_name (str): unique name for an item
        platform (Optional[Platform], optional): platform. Defaults to Platform.pc.
        include (Optional[IncludeOption], optional):
            additional info.
            If ``IncludeOption.item`` is set, the info of the item will be returned additionally.
            Defaults to None.

    Returns:
        Union[List[OrderRow], Tuple[List[OrderRow], ItemFull, List[ItemFull]]]:
            The first is the order list.
            If ``IncludeOption.item`` is set, the same result of get_item method will be returned
            as the 2nd and 3rd return value.
    """
    res = requests.get(
        API_BASE_URL + f"/items/{url_name}/orders",
        params={"include": include.value if include is not None else None},
        headers={"Platform": platform.value},
    )
    check_wm_response(res)
    json_obj = res.json()
    orders = list(map(lambda x: OrderRow.from_dict(x), json_obj["payload"]["orders"]))
    if include == IncludeOption.item:
        target_item, items_in_set = _transform_item_result(json_obj["include"]["item"])
        return orders, target_item, items_in_set
    else:
        return orders


def get_current_orders(sess: Session) -> Tuple[List[OrderItem], List[OrderItem]]:
    """Get orders of current profile. See ``get_orders_by_username``

    Args:
        sess: session

    Returns:
        Tuple[List[OrderItem], List[OrderItem]]:
            the first is the list of the buy orders, the second is the list of sell orders
    """
    if sess.user.ingame_name is None or sess.user.ingame_name.strip() == "":
        raise RuntimeError("`ingame_name` of session is invalid.", sess)
    return get_orders_by_username(sess.user.ingame_name, sess)


def get_orders_by_username(
    username: str, sess: Optional[Session] = None
) -> Tuple[List[OrderItem], List[OrderItem]]:
    """Get orders of user

    Args:
        username (str): username
        sess (Optional[Session]): session. If None, then set in guest mode. Defaults to None.

    Returns:
        Tuple[List[OrderItem], List[OrderItem]]:
            the first is the list of the buy orders, the second is the list of sell orders
    """
    if sess is not None:
        res = requests.get(
            API_BASE_URL + f"/profile/{username}/orders",
            **sess.to_header_dict(),
        )
    else:
        res = requests.get(
            API_BASE_URL + f"/profile/{username}/orders",
        )
    check_wm_response(res)
    json_obj = res.json()
    return (
        list(map(lambda x: OrderItem.from_dict(x), json_obj["payload"]["buy_orders"])),
        list(map(lambda x: OrderItem.from_dict(x), json_obj["payload"]["sell_orders"])),
    )


def get_individual_order(sess: Session, order_id: str) -> OrderItem:
    """Get individual order by ``order_id``

    Args:
        sess (Session): session
        order_id (str): ``id`` of order

    Returns:
        OrderItem: order
    """
    raise NotImplementedError("Seems totally deprecated since response body is empty")
    # res = requests.get(
    #     API_BASE_URL + f"/profile/orders/{order_id}",
    #     **sess.to_header_dict(),
    # )
    # check_wm_response(res)
    # json_obj = res.json()
    # return OrderItem.from_dict(json_obj["payload"]["order"])


def add_order(sess: Session, new_item: OrderNewItem) -> OrderItem:
    """Add new order

    Args:
        sess (Session): session
        new_item (OrderNewItem): new item to be created

    Returns:
        OrderItem: new order
    """
    res = requests.post(
        API_BASE_URL + "/profile/orders",
        json=asdict(new_item, filter=dataclass_filter, value_serializer=dataclass_value_serializer),
        **sess.to_header_dict(),
    )
    check_wm_response(res)
    json_obj = res.json()
    return OrderItem.from_dict(json_obj["payload"]["order"])


def update_order(sess: Session, order_id: str, updated_item: OrderUpdateItem) -> OrderItem:
    """Update an order

    TODO: includes ``top``

    Args:
        sess (Session): session
        order_id (str): ``id`` of order
        updated_item (OrderUpdateItem): updated item

    Returns:
        OrderItem: updated order
    """
    req_json = {"order_id": order_id}
    req_json.update(
        asdict(updated_item, filter=dataclass_filter, value_serializer=dataclass_value_serializer)
    )
    res = requests.put(
        API_BASE_URL + f"/profile/orders/{order_id}",
        json=req_json,
        **sess.to_header_dict(),
    )
    check_wm_response(res)
    json_obj = res.json()
    return OrderItem.from_dict(json_obj["payload"]["order"])


def delete_order(sess: Session, order_id: str) -> None:
    """Delete an order

    Args:
        sess (Session): session
        order_id (str): ``id`` of order

    Returns:
        None
    """
    res = requests.delete(
        API_BASE_URL + f"/profile/orders/{order_id}",
        **sess.to_header_dict(),
    )
    check_wm_response(res)
