"""
    Arcane - A secure remote desktop application for Windows with the
    particularity of having a server entirely written in PowerShell and
    a cross-platform client (Python/QT6).

    Author: Jean-Pierre LESUEUR (@DarkCoderSc)
    License: Apache License 2.0
    https://github.com/PhrozenIO
    https://github.com/DarkCoderSc
    https://twitter.com/DarkCoderSc
    www.phrozen.io
"""

from enum import Enum, auto


class ArcaneProtocolError(Enum):
    AuthenticationFailed = auto()
    ResourceNotFound = auto()
    InvalidStructureData = auto()
    UnsupportedVersion = auto()


class ArcaneProtocolException(Exception):
    def __init__(self, reason: ArcaneProtocolError):
        self.reason = reason

        error_messages = {
            ArcaneProtocolError.AuthenticationFailed: "Authentication failed",
            ArcaneProtocolError.ResourceNotFound: "A resource was not found",
            ArcaneProtocolError.InvalidStructureData: "Invalid structure data, whether corrupted or missing properties",
        }

        super().__init__(error_messages.get(reason, "Unknown error"))