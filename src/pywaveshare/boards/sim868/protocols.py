import abc
import re
import typing

from . import config


class SupportedProtocol(abc.ABC):
    NAME: typing.Optional[str] = None

    RESPONSE_PATTERN = r""


class SMS(SupportedProtocol):
    NAME = "SMS"

    RESPONSE_PATTERN = (
        r"loremipsumdolorsitamet"
        r"loremipsumdolorsitamet"
        r"loremipsumdolorsitamet"
        r"loremipsumdolorsitamet"
        r"loremipsumdolorsitamet"
        r"loremipsumdolorsitamet"
        r"loremipsumdolorsitamet"
    )


def get_enabled_protocols(config: config.Config) -> typing.List[SupportedProtocol]:
    return []


if __name__ == "__main__":
    protocol = SMS()
    print(protocol.RESPONSE_PATTERN)
    DATA = "OK\r\n"
    match = re.fullmatch(r"OK\r\n", DATA)
    print(match)
    print(match.string if match is not None else None)
