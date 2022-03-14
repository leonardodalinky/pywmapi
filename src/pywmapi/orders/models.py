from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from dacite import Config

from ..auth.models import UserShort
from ..common import *

__all__ = [
    "OrderType",
    "OrderCommon",
    "OrderRow",
    # "OrderFull",
]


@dataclass
class OrderCommon(ModelBase):
    id: str
    platinum: int
    quantity: int
    order_type: OrderType
    platform: Platform
    region: Optional[str]
    creation_date: datetime
    last_update: datetime
    visible: bool


@dataclass
class OrderRow(OrderCommon):
    user: UserShort


@dataclass
class OrderFull(OrderRow):
    # TODO
    def __init__(self):
        raise NotImplementedError()
