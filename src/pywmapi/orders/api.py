from typing import Dict, List, Optional, Tuple, Union

import requests

from ..common import *
from ..exceptions import *
from ..items.api import _transform_item_result
from ..items.models import *
from .models import *

__all__ = [
    "get_orders",
]


def get_orders(
    url_name: str,
    platform: Optional[Platform] = Platform.pc,
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
        params={"include": include},
        headers={"Platform": platform},
    )
    check_wm_response(res)
    json_obj = res.json()
    orders = list(map(lambda x: OrderRow.from_dict(x), json_obj["payload"]["orders"]))
    if include == IncludeOption.item:
        target_item, items_in_set = _transform_item_result(json_obj["include"]["item"])
        return orders, target_item, items_in_set
    else:
        return orders
