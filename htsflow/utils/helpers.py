from enum import IntEnum, Flag


def print_flag(
    print_enum: Flag,
) -> None:
    pl: list[str] = []
    for e in print_enum:
        vs = '-'.join([str(int(e.value)), str(hex(e.value)), str(bin(e.value))])
        pl.append(f'{e}: {vs}')
    print(pl)


def print_enum(
    print_enum: IntEnum
) -> None:
    print([e for e in print_enum])  # pyright: ignore[reportGeneralTypeIssues, reportUnknownArgumentType, reportUnknownVariableType] - iterating works fine
