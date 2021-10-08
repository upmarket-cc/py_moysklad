from dataclasses import dataclass

from py_moysklad.entities.meta import Meta
from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class Attribute(MetaEntity):
    # private Type type
    # private Meta.Type entityType
    value: dict
    required: bool
    download: Meta
    customEntityMeta: Meta
    description: str
    # private transient Meta.Type attributeEntityType
