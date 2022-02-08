from typing import Dict, Any, Optional, Type, TypeVar
from dacite import from_dict, Config
from enum import Enum
from datetime import datetime


T = TypeVar("T")


class ModelBase:
    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        # MAY be overrided by subclass in need
        return cls._from_dict(d)

    @classmethod
    def _from_dict(cls: Type[T], d: Dict[str, Any], config: Optional[Config] = Config()) -> T:
        if Enum not in config.cast:
            config.cast.append(Enum)
        if datetime not in config.type_hooks.keys():
            config.type_hooks[datetime] = datetime.fromisoformat
        return from_dict(data_class=cls, data=d, config=config)
