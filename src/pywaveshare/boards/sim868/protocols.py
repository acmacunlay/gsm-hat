import abc
import re
import typing


class SupportedStandard(abc.ABC):
    NAME: typing.Optional[str] = None

    RESPONSE_PATTERN = r""


class SMS(SupportedStandard):
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


class SupportedProtocolFactory:
    pass


if __name__ == "__main__":
    protocol = SMS()
    print(protocol.RESPONSE_PATTERN)
    DATA = "OK\r\n"
    match = re.fullmatch(r"OK\r\n", DATA)
    print(match)
    print(match.string if match is not None else None)
