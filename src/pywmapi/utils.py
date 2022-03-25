from typing import Dict


def dataclass_ignore_none_factory(x) -> Dict:
    """used as ``dict_factory`` in function ``dataclasses.asdict`` to removed ``None` field in the result json dict.

    Args:
        x: object

    Returns:
        Dict:
    """
    return {k: v for (k, v) in x if v is not None}
