from typing import List, Optional, Union

from attrs import define

from ...common import AuctionType, ElementType, ModelBase, Platform, Polarity

__all__ = [
    "AttributeInRiven",
    "RivenAuction",
    "LichAuction",
    "KubrowAuction",
    "AuctionType",
    "AuctionEntry",
]


@define
class AttributeInRiven:
    positive: bool
    value: int
    url_name: str


@define
class RivenAuction:
    attributes: List[AttributeInRiven]
    name: str
    mastery_level: int
    re_rolls: int
    weapon_url_name: str
    polarity: Polarity
    mod_rank: int
    type: AuctionType = AuctionType.riven


@define
class LichAuction:
    weapon_url_name: str
    element: ElementType
    damage: int
    ephemera: bool
    quirk: str
    name: Optional[str]
    type: AuctionType = AuctionType.lich


@define
class KubrowAuction:
    name: Optional[str]
    type: AuctionType = AuctionType.kubrow


@define
class AuctionEntry(ModelBase):
    id: str
    minimal_reputation: int
    winner: Optional[str]
    private: bool
    visible: bool
    note_raw: str
    note: str
    owner: str
    starting_price: int
    buyout_price: Optional[int]
    minimal_increment: Optional[int]
    is_direct_sell: bool
    top_bid: Optional[int]
    created: str
    updated: str
    platform: Platform
    closed: bool
    is_marked_for: Optional[str]
    marked_operation_at: Optional[str]
    item: Union[RivenAuction, LichAuction, KubrowAuction]
