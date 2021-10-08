from dataclasses import dataclass

from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class Group(MetaEntity):
    index: int
