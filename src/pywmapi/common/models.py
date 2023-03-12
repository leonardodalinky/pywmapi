from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Generic, Optional, Type, TypeVar

from dacite import Config, from_dict

from .enums import WSType

T = TypeVar("T")


__all__ = [
    "ModelBase",
    "WSMessage",
]


def _transform_underscore(d: Dict[str, Any]) -> Dict[str, Any]:
    """transform "-" to "_" recursively

    Args:
        d:

    Returns:
        Dict[str, Any]: new dict
    """
    new_dict = d.copy()
    for k, v in new_dict.items():
        if isinstance(v, Dict):
            new_dict[k] = _transform_underscore(v)
    for k in list(new_dict.keys()):
        if "-" in k:
            new_dict[k.replace("-", "_")] = new_dict[k]
            del new_dict[k]
    return new_dict


class ModelBase:
    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        # MAY be overridden by subclass in need
        return cls._from_dict(d)

    @classmethod
    def _from_dict(cls: Type[T], d: Dict[str, Any], config: Optional[Config] = Config()) -> T:
        if Enum not in config.cast:
            config.cast.append(Enum)
        if datetime not in config.type_hooks.keys():
            config.type_hooks[datetime] = datetime.fromisoformat
        return from_dict(data_class=cls, data=_transform_underscore(d), config=config)


@dataclass(init=False)
class WSMessage(Generic[T]):
    type: WSType
    payload: T

    def __init__(self, type: WSType, payload: Type[T]) -> None:
        super().__init__()
        self.type = type
        self.payload: Type[T] = payload
