import json
from datetime import datetime
from enum import Enum
from functools import partial
from queue import Queue
from threading import Thread
from typing import Any, Dict, Optional, TypeVar

from attrs import asdict, define
from websocket import ABNF, WebSocketApp

from ..common import *
from ..exceptions import *
from ..utils import *

__all__ = [
    "Session",
    "UserShort",
    "User",
]


T = TypeVar("T")


class Session:
    jwt: str
    user: "User"
    ws_platform: Platform
    recv_messages: Queue
    _is_ws_open: bool
    _wsapp: WebSocketApp
    _wsapp_thread: Thread

    def __init__(
        self,
        jwt: str,
        user: "User",
        ws_platform: Platform,
        on_message: Optional[MessageCallback],
    ) -> None:
        self.jwt = jwt
        self.user = user
        self.ws_platform = ws_platform
        self.recv_messages = Queue()
        self._is_ws_open = False

        def _ws_on_open(wsapp: WebSocketApp):
            self._is_ws_open = True

        def _ws_on_message(wsapp: WebSocketApp, message: str, out_queue: Queue):
            out_queue.put(message)
            if on_message is not None:
                on_message(message)

        def _wsapp_func():
            self._wsapp = WebSocketApp(
                WSS_BASE_URL + f"?platform={ws_platform.value}",
                cookie=f"JWT={jwt}",
                on_open=_ws_on_open,
                on_message=partial(_ws_on_message, out_queue=self.recv_messages),
            )
            self._wsapp.run_forever()

        self._wsapp_thread = Thread(target=_wsapp_func)
        self._wsapp_thread.daemon = True
        self._wsapp_thread.start()

    def send_str(self, data: str, opcode: int = ABNF.OPCODE_TEXT) -> None:
        """Send raw string data through ws connection

        Args:
            data (str): raw string data
            opcode (int, optional): ws opcode. Defaults to ABNF.OPCODE_TEXT.
        """
        while not self._is_ws_open:
            continue
        try:
            self._wsapp.send(data, opcode=opcode)
        except Exception as e:
            raise WMError(-1, "Websocket failed. Try to dive into the `raw_error`.", e)

    def send_msg(self, msg_data: WSMessage[T], opcode: int = ABNF.OPCODE_TEXT) -> None:
        data = json.dumps(
            asdict(msg_data, filter=dataclass_filter, value_serializer=dataclass_value_serializer)
        )
        self.send_str(data, opcode=opcode)

    def __del__(self):
        self._wsapp.close()

    def to_header_dict(self) -> Dict[str, Any]:
        """get the key/value dict for request header

        Returns:
            Dict[str, Any]:
        """
        return {
            "headers": {"Authorization": self.jwt},
        }


@define
class UserShort:
    class Status(Enum):
        ingame = "ingame"
        online = "online"
        offline = "offline"

    id: str
    status: Status
    region: str
    reputation: int
    last_seen: datetime
    ingame_name: Optional[str] = None
    """In-game name. Only get this field when `verification=True`."""
    avatar: Optional[str] = None


@define
class User(ModelBase):
    class Role(Enum):
        anonymous = "anonymous"
        user = "user"
        moderator = "moderator"
        admin = "admin"

    class PatreonBadge(Enum):
        bronze = "bronze"
        gold = "gold"
        silver = "silver"
        platinum = "platinum"

    @define
    class PatreonProfile:
        patreon_founder: bool
        subscription: bool
        patreon_badge: str

    @define
    class LinkedAccounts:
        steam_profile: bool
        patreon_profile: bool
        xbox_profile: bool
        discord_profile: bool

    id: str
    """User ID."""
    anonymous: bool
    verification: bool
    """Whether the user is verified."""
    check_code: str
    platform: Platform
    region: str
    banned: bool
    role: Role
    linked_accounts: LinkedAccounts
    # `has_mail` is spelled as `has_email` mistakenly in the official api docs
    has_mail: bool
    written_reviews: int
    unread_messages: int
    ingame_name: Optional[str] = None
    """In-game name. Only get this field when `verification=True`."""
    patreon_profile: Optional[PatreonProfile] = None
    ban_reason: Optional[str] = None
    avatar: Optional[str] = None
    background: Optional[str] = None
