from typing import Optional

__all__ = [
    "WMError",
]


class WMError(Exception):
    """Base exception for pywmapi"""

    def __init__(self, status_code: int, error_msg: Optional[str], raw_error: Exception) -> None:
        super().__init__(status_code, error_msg, raw_error)
        self.status_code = status_code
        self.error_msg = error_msg
        self.raw_error = raw_error

    def __str__(self) -> str:
        return f"{self.status_code} {self.error_msg}"

    def __repr__(self) -> str:
        return self.__str__()
