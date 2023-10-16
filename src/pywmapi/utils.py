from enum import Enum
from typing import Any

from attrs import Attribute


def dataclass_filter(_attribute: Attribute, value: Any) -> bool:
    return value is not None


def dataclass_value_serializer(_inst, _field, value) -> Any:
    if isinstance(value, Enum):
        return value.value
    return value
