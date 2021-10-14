from py_moysklad.entities.entity import Entity
from py_moysklad.entities.meta import Meta


class MetaEntity(Entity):
    id: str  # noqa: VNE003
    accountId: str
    name: str
    meta: Meta
