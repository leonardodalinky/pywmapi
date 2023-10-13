from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from ..auth.models import UserShort
from ..common import *

__all__ = [
    "OrderType",
    "OrderCommon",
    "OrderRow",
    "OrderItem",
    # "OrderFull",
    "OrderNewItemBase",
    "OrderNewItem",
    "OrderUpdateItem",
]


@dataclass
class OrderCommon(ModelBase):
    id: str
    platinum: int
    quantity: int
    order_type: OrderType
    platform: Platform
    region: Optional[str]
    creation_date: Optional[datetime]
    closed_date: Optional[datetime]
    last_update: Optional[datetime]
    visible: bool
    subtype: Optional[Subtype]
    mod_rank: Optional[int]


@dataclass
class OrderRow(OrderCommon):
    user: UserShort


@dataclass
class OrderItem(OrderCommon):
    @dataclass
    class ItemInOrder(ModelBase):
        @dataclass
        class LangInOrderItem:
            item_name: str

        id: str
        url_name: str
        icon: str
        thumb: str
        sub_icon: Optional[str]
        quantity_for_set: Optional[int]
        mod_max_rank: Optional[int]
        # only for relics and fishes
        subtypes: Optional[List[str]]
        tags: List[str]
        cyan_stars: Optional[int]
        amber_stars: Optional[int]
        ducats: Optional[int]
        # language items
        en: Optional[LangInOrderItem]
        ru: Optional[LangInOrderItem]
        ko: Optional[LangInOrderItem]
        de: Optional[LangInOrderItem]
        fr: Optional[LangInOrderItem]
        pt: Optional[LangInOrderItem]
        zh_hant: Optional[LangInOrderItem]
        zh_hans: Optional[LangInOrderItem]
        es: Optional[LangInOrderItem]
        it: Optional[LangInOrderItem]
        pl: Optional[LangInOrderItem]

    user: Optional[UserShort]
    item: ItemInOrder


@dataclass
class OrderFull(OrderRow):
    # TODO
    def __init__(self):
        raise NotImplementedError()


@dataclass
class OrderNewItemBase(ModelBase):
    platinum: int
    quantity: int
    rank: Optional[int]
    subtype: Optional[Subtype]
    visible: bool


@dataclass
class OrderNewItem(OrderNewItemBase):
    """
    Request class for ``orders.add_new_order`` and others.
    """

    item_id: str
    order_type: OrderType


@dataclass
class OrderUpdateItem(OrderNewItemBase):
    """
    Request class for ``orders.update_order``
    """

    pass
