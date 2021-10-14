from dataclasses import dataclass
from enum import Enum

from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class Barcode(MetaEntity):
    type: "Type"
    value: str

    class Type(Enum):
        EAN13 = "EAN13"
        EAN8 = "EAN8"
        CODE128 = "CODE128"
        GTIN = "GTIN"
        UPC = "UPC"
