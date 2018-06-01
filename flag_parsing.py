from typing import List
import itertools as it
import csv


def parse(input: str):
    reader = csv.reader(input.split("\n"))
    return list(map(parse_fields, reader))

def parse_fields(row: List[str]):
    for i in it.chain(range(1, 17), range(18, 28)):
        row[i] = int(row[i])
    return row
