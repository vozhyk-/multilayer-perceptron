from typing import List
import itertools as it
import csv


def parse(input: str) -> List[list]:
    lines = input.split("\n")
    nonempty_lines = filter(lambda line: line != "", lines)
    reader = csv.reader(nonempty_lines)
    return list(map(parse_fields, reader))

def parse_fields(row: List[str]):
    for i in range(2):
        row[i] = int(row[i])

    for i in range(2, 34):
        row[i] = float(row[i])

    row[34] = goodbad_to_number(row[34])

    return row

def goodbad_to_number(input: str) -> int:
    if input == "g":
        return 1
    elif input == "b":
        return 0
