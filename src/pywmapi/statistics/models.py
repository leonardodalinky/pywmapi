from datetime import datetime
from typing import List, Optional

from attrs import define, field

from ..common import *

__all__ = [
    "StatisticClosed",
    "StatisticLive",
    "Statistic",
]


@define
class StatisticClosed(ModelBase):
    datetime: datetime
    volume: int
    min_price: float
    max_price: float
    open_price: float
    closed_price: float
    avg_price: float
    wa_price: float
    median: float
    donch_top: int
    donch_bot: int
    id: str
    moving_avg: Optional[float] = None
    mod_rank: Optional[int] = None


@define
class StatisticLive(ModelBase):
    datetime: datetime
    volume: int
    min_price: float
    max_price: float
    avg_price: float
    wa_price: float
    median: float
    order_type: OrderType
    id: str
    moving_avg: Optional[float] = None
    mod_rank: Optional[int] = None


@define
class Statistic:
    closed_48h: List[StatisticClosed]
    closed_90d: List[StatisticClosed]
    live_48h: List[StatisticLive]
    live_90d: List[StatisticLive]
