from typing import List, Optional

from attrs import define

from ..common import *

__all__ = [
    "LangInItem",
]


@define
class LangInItem(ModelBase):
    @define
    class Drop:
        name: str
        link: Optional[str]

    item_name: str
    description: str
    wiki_link: Optional[str]
    drop: List[Drop]
