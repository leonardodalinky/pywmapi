import dataclasses
import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from functools import partial
from queue import Queue
from threading import Thread
from typing import Dict, Optional, TypeVar

from dacite import Config
from websocket import ABNF, WebSocketApp

from ..common import *
from ..exceptions import *

__all__ = [
    "Session",
    "UserShort",
    "User",
]


T = TypeVar("T")


class Session:
    def __init__(
        self,
        jwt: str,
        csrf_token: str,
        user: "User",
        ws_platform: Platform,
        on_message: Optional[MessageCallback],
    ) -> None:
        self.jwt = jwt
        self.csrf_token = csrf_token
        self.user = user
        self.ws_platform = ws_platform
        self.recv_messages = Queue()
        self._is_ws_open = False
        self._wsapp: Optional[WebSocketApp] = None

        def _ws_on_open(wsapp: WebSocketApp):
            self._is_ws_open = True

        def _ws_on_message(wsapp: WebSocketApp, message: str, out_queue: Optional[Queue] = None):
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
        self._wsapp_thread.setDaemon(True)
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
        data = json.dumps(dataclasses.asdict(msg_data))
        self.send_str(data, opcode=opcode)

    def __del__(self):
        self._wsapp.close()

    def to_header_dict(self) -> Dict[str, Dict[str, str]]:
        """get the key/value dict for request header

        Returns:
            Dict[str, Dict[str, str]]:
        """
        return {
            "headers": {"X-CSRFToken": self.csrf_token},
            "cookies": {"JWT": self.jwt},
        }


@dataclass
class UserShort:
    class Status(str, Enum):
        ingame = "ingame"
        online = "online"
        offline = "offline"

    id: str
    ingame_name: str
    status: Status
    region: str
    reputation: int
    avatar: Optional[str]
    last_seen: datetime


@dataclass
class User(ModelBase):
    class Role(str, Enum):
        anonymous = "anonymous"
        user = "user"
        moderator = "moderator"
        admin = "admin"

    class PatreonBadge(str, Enum):
        bronze = "bronze"
        gold = "gold"
        silver = "silver"
        platinum = "platinum"

    @dataclass
    class PatreonProfile:
        patreon_founder: bool
        subscription: bool
        patreon_badge: str

    @dataclass
    class LinkedAccounts:
        steam_profile: bool
        patreon_profile: bool
        xbox_profile: bool
        discord_profile: bool

    id: str
    anonymous: bool
    verification: bool
    check_code: str
    ingame_name: str
    patreon_profile: Optional[PatreonProfile]
    platform: Platform
    region: str
    banned: bool
    ban_reason: Optional[str]
    role: Role
    avatar: str
    background: Optional[str]
    linked_accounts: LinkedAccounts
    # `has_mail` is spelled as `has_email` mistakenly in the official api docs
    has_mail: bool
    written_reviews: int
    unread_messages: int
