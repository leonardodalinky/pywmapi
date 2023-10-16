from typing import Optional, Union

import requests
from attrs import asdict

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
) -> AuctionEntry:
    """Create an auction

    Args:
        sess (Session): session
        item (Union[RivenAuction, LichAuction, KubrowAuction]): item of the auction
        starting_price (int): start price
        buyout_price (Optional[int]): buyout price. If None, set to infinity.
        note (str): description
        minimal_reputation (int): minimal reputation required to buy
        minimal_increment (int): minimal increment
        private (bool): private auction

    Returns:
        AuctionEntry: entry of the created auction
    """
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
        **sess.to_header_dict(),
    )
    check_wm_response(res)
    return AuctionEntry.from_dict(res.json()["payload"]["auctions"])
