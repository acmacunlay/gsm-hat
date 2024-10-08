import abc
import typing


class SupportedProtocol(abc.ABC):
    NAME: typing.Optional[str] = None

    RESPONSE_PATTERN = r""
