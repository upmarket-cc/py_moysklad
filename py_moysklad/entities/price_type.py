from dataclasses import dataclass

from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class PriceType(MetaEntity):
    externalCode: str
