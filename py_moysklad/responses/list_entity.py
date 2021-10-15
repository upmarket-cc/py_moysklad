from typing import Generic, List, TypeVar

from py_moysklad.entities.meta_entity import MetaEntity


T = TypeVar('T', bound=MetaEntity)


class ListEntity(MetaEntity, Generic[T]):
    context: dict  # FIXME
    rows: List[T]
