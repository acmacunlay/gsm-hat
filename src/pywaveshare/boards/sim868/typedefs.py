import typing

SMSSend = typing.TypedDict(
    "SMSSend",
    {
        "Recipients": typing.List[str],
        "Message": str,
    },
)
