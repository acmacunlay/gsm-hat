import typing

import typing_extensions

SMSSend = typing_extensions.TypedDict(
    "SMSSend",
    {
        "Recipients": typing.List[str],
        "Message": str,
    },
)
