from typing import Generic, List, Optional, TypeVar

from py_moysklad.entities.meta_entity import MetaEntity


T = TypeVar("T", bound=MetaEntity)


class ListEntity(MetaEntity, Generic[T]):
    context: Optional[dict]  # FIXME
    rows: Optional[List[T]]
