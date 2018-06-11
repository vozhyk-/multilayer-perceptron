from typing import List

import parsing.flags
import flag_dataset


def read_flag_dataset() -> List[flag_dataset.FlagsRow]:
    with open("data/flags/flag.data") as file:
        input = file.read()
    parsed = parsing.flags.parse(input)
    return list(map(flag_dataset.FlagsRow, parsed))
