from dataclasses import dataclass
from typing import List, Optional

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
