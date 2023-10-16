from enum import Enum
from typing import Dict


def dataclass_wm_factory(x) -> Dict:
    """Used as `dict_factory` in function `dataclasses.asdict` to remove `None` field in the result json dict.

    Args:
        x: object

    Returns:
        Dict:
    """

    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.value
        return obj

    return {k: convert_value(v) for k, v in x if v is not None}
