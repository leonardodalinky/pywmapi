from typing import Dict, List, Optional, Tuple, Union
from warnings import warn

import requests

from pywmapi.auction.model import AuctionItem, Auction

__all__ = [
    "create_auction",
    # "get_item",
]

from pywmapi.auth import get_csrf_and_jwt
from pywmapi.common import API_BASE_URL
from pywmapi.exceptions import check_wm_response


def create_auction(
        note: str,
        starting_price: int,
        buyout_price: int,
        minimal_reputation: int,
        minimal_increment: int,
        private: bool,
        item: AuctionItem
):
    """Create auction, for riven or lich item types.

        Args:
            lang (Optional[Language], optional): addition language support. Defaults to Language.en.

        Returns:
            List[ItemShort]: items
    """
    csrf_token, jwt = get_csrf_and_jwt()
    res = requests.post(
        API_BASE_URL + "/auction/create",
        json={
            "note": note,
            "starting_price": starting_price,
            "buyout_price": buyout_price,
            "minimal_reputation": minimal_reputation,
            "minimal_increment": minimal_increment,
            "private": private,
            "item": item,
        },
        headers={"X-CSRFToken": csrf_token},
        cookies={"JWT": jwt},
    )
    check_wm_response(res)
    # auction = Auction.from_dict(res.json()["payload"]["auction"])

