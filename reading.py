from typing import List

import parsing.flags
import parsing.horse_colic
import parsing.ionosphere
import flag_dataset
import horse_colic_dataset
import ionosphere_dataset


def read_flag_dataset() -> List[flag_dataset.FlagsRow]:
    return _read_dataset("data/flags/flag.data", parsing.flags, flag_dataset.FlagsRow)

def read_horse_colic_training_dataset() -> List[horse_colic_dataset.HorseColicRow]:
    return _read_horse_colic_dataset("data/horse-colic/horse-colic.data")

def read_horse_colic_test_dataset() -> List[horse_colic_dataset.HorseColicRow]:
    return _read_horse_colic_dataset("data/horse-colic/horse-colic.test")

def _read_horse_colic_dataset(filename: str) -> List[horse_colic_dataset.HorseColicRow]:
    return _read_dataset(filename,
        parsing.horse_colic, horse_colic_dataset.HorseColicRow)

def read_ionosphere_dataset() -> List[ionosphere_dataset.IonosphereRow]:
    return _read_dataset("data/ionosphere/ionosphere.data", parsing.ionosphere, ionosphere_dataset.IonosphereRow)

def _read_dataset(filename: str, parsing_module, row_class: type):
    with open(filename) as file:
        input = file.read()
    parsed = parsing_module.parse(input)
    return list(map(row_class, parsed))
