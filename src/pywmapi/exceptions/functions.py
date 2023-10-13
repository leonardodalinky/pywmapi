from typing import Any, Dict

from requests import Response

from .defs import *

__all__ = [
    "check_wm_response",
]


def check_wm_response(res: Response) -> None:
    try:
        res.raise_for_status()
    except Exception as e:
        if res.text.strip() == "":
            return
        res_json: Dict[str, Any] = res.json()
        if res_json.get("error", None) is not None:
            raise WMError(
                res.status_code,
                error_msg=res_json["error"],
                raw_error=e,
            )
        raise WMError(
            res.status_code,
            error_msg=None,
            raw_error=e,
        )
