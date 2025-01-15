from datetime import datetime
from typing import List, Optional

from attrs import define, field

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


@define
class OrderCommon(ModelBase):
    id: str
    platinum: int
    quantity: int
    order_type: OrderType
    visible: bool
    platform: Optional[Platform] = None
    region: Optional[str] = None
    creation_date: Optional[datetime] = None
    closed_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    subtype: Optional[Subtype] = None
    mod_rank: Optional[int] = None


@define(kw_only=True)
class OrderRow(OrderCommon):
    user: UserShort


@define(kw_only=True)
class OrderItem(OrderCommon):
    @define
    class ItemInOrder(ModelBase):
        @define
        class LangInOrderItem:
            item_name: str

        id: str
        url_name: str
        icon: str
        thumb: str
        # only for relics and fishes
        tags: List[str]
        sub_icon: Optional[str] = None
        quantity_for_set: Optional[int] = None
        mod_max_rank: Optional[int] = None
        subtypes: Optional[List[str]] = None
        cyan_stars: Optional[int] = None
        amber_stars: Optional[int] = None
        ducats: Optional[int] = None
        # language items
        en: Optional[LangInOrderItem] = None
        ru: Optional[LangInOrderItem] = None
        ko: Optional[LangInOrderItem] = None
        de: Optional[LangInOrderItem] = None
        fr: Optional[LangInOrderItem] = None
        pt: Optional[LangInOrderItem] = None
        zh_hant: Optional[LangInOrderItem] = None
        zh_hans: Optional[LangInOrderItem] = None
        es: Optional[LangInOrderItem] = None
        it: Optional[LangInOrderItem] = None
        pl: Optional[LangInOrderItem] = None

    item: ItemInOrder
    user: Optional[UserShort] = None
    platform: Optional[Platform] = None


@define(kw_only=True)
class OrderFull(OrderRow):
    # TODO
    def __init__(self):
        raise NotImplementedError()


@define(kw_only=True)
class OrderNewItemBase(ModelBase):
    platinum: int
    quantity: int
    visible: bool
    rank: Optional[int] = None
    subtype: Optional[Subtype] = None


@define(kw_only=True)
class OrderNewItem(OrderNewItemBase):
    """
    Request class for ``orders.add_new_order`` and others.
    """

    item_id: str
    order_type: OrderType


@define(kw_only=True)
class OrderUpdateItem(OrderNewItemBase):
    """
    Request class for ``orders.update_order``
    """

    pass
