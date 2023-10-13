from typing import Dict, List, Optional, Tuple

import requests

from ..common import *
from ..exceptions import *
from .models import *

__all__ = [
    "get_statistic",
]


def get_statistic(url_name: str, platform: Platform = Platform.pc) -> Statistic:
    """Get statistic of an item

    Args:
        url_name (str): unique name for an item
        platform (Optional[Platform], optional): platform. Defaults to Platform.pc.

    Returns:
        Statistic: statistic over the past 48h/90d period
    """
    res = requests.get(
        API_BASE_URL + f"/items/{url_name}/statistics",
        headers={"Platform": platform.value},
    )
    check_wm_response(res)
    payload = res.json()["payload"]
    return Statistic(
        closed_48h=list(
            map(
                lambda x: StatisticClosed.from_dict(x),
                payload["statistics_closed"]["48hours"],
            )
        ),
        closed_90d=list(
            map(
                lambda x: StatisticClosed.from_dict(x),
                payload["statistics_closed"]["90days"],
            )
        ),
        live_48h=list(
            map(
                lambda x: StatisticLive.from_dict(x),
                payload["statistics_live"]["48hours"],
            )
        ),
        live_90d=list(
            map(
                lambda x: StatisticLive.from_dict(x),
                payload["statistics_live"]["90days"],
            )
        ),
    )
