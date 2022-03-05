from dataclasses import dataclass
from datetime import time
from typing import Any, Dict, List, Optional

from pywmapi.common import ModelBase, Platform, AuctionItemType, Polarity


@dataclass
class AttributeInRiven(ModelBase):
    @dataclass
    class attributes:
        positve: bool
        value: int
        url_name: str


@dataclass
class AuctionItem:
    type: AuctionItemType
    attributes: Optional[AttributeInRiven]
    name: str
    mastery_level: int
    re_rolls: int
    weapon_url_name: str
    polarity: Polarity
    mod_rank: int


@dataclass
class Auction(ModelBase):
    id: str
    minimal_reputation: int
    winner: Optional
    private: bool
    visible: bool
    note_raw: str
    note: str
    owner: str
    starting_price: int
    buyout_price: Optional
    minimal_increment: int
    is_direct_sell: bool
    top_bid: Optional
    created: str
    updated: str
    platform: Platform
    closed: bool
    is_marked_for: Optional
    marked_operation_at: Optional
    item: AuctionItem
