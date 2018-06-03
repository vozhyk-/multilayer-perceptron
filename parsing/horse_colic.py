from typing import List
import csv


def parse(input: str):
    lines = input.split("\n")
    nonempty_lines = filter(lambda line: line != "", lines)
    reader = csv.reader(nonempty_lines, delimiter=" ")
    return list(map(parse_fields, reader))

def parse_fields(row: List[str]):
    # Remove the always-empty field at the end
    row = row[:28]
    parsed = list(map(lambda i: convert_field(*i), enumerate(row)))
    return convert_lesion_types(parsed)

def convert_field(index, field):
    if field == "?":
        return None
    if index in list(range(3)) + list(range(4, 15)) + [16, 17, 20, 22, 23, 27]:
        return int(field)
    if index in [3, 15, 18, 19, 21]:
        return float(field)
    # 24, 25, 26: keep it a string;
    # but it should really be parsed and expanded into a few fields.
    return field

def convert_lesion_types(row: list):
    return \
        row[:24] + \
        convert_lesion_type(row[24]) + \
        convert_lesion_type(row[25]) + \
        convert_lesion_type(row[26]) + \
        row[27:]

def convert_lesion_type(input: str):
    if input.startswith("0") or input.startswith("11"):
        subfield_digits = [2, 1, 1, 1]
    else:
        subfield_digits = [1, 1, 1, 2]

    result = []
    i = 0
    for digits in subfield_digits:
        result.append(int(input[i:i+digits]))
        i += digits
    return result
