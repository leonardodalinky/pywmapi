from typing import List, Optional, Union

import requests
from dataclasses import asdict

from ...auth.models import Session
from ...common import *
from ...exceptions import *
from .models import AuctionEntry, KubrowAuction, LichAuction, RivenAuction

__all__ = [
    "create_auction",
    # "get_item",
]


def create_auction(
    sess: Session,
    item: Union[RivenAuction, LichAuction, KubrowAuction],
    starting_price: int,
    buyout_price: Optional[int],
    note: str,
    minimal_reputation: int = 0,
    minimal_increment: int = 1,
    private: bool = False,
):
    res = requests.post(
        API_BASE_URL + "/auctions/create",
        json={
            "note": note,
            "starting_price": starting_price,
            "buyout_price": buyout_price,
            "minimal_reputation": minimal_reputation,
            "minimal_increment": minimal_increment,
            "private": private,
            "item": asdict(item),
        },
        headers={"X-CSRFToken": sess.csrf_token},
        cookies={"JWT": sess.jwt},
    )
    check_wm_response(res)
    return AuctionEntry.from_dict(res.json()["payload"]["auctions"])
