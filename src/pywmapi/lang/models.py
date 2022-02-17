from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from dacite import Config

from ..common import *

__all__ = [
    "LangInItem",
]


@dataclass
class LangInItem(ModelBase):
    @dataclass
    class Drop:
        name: str
        link: Optional[str]

    item_name: str
    description: str
    wiki_link: Optional[str]
    drop: List[Drop]
