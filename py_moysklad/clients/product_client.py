import typing
from abc import ABC, abstractmethod

from py_moysklad.entities.meta_entity import MetaEntity
from py_moysklad.entities.products.product import Product
from py_moysklad.responses.list_entity import ListEntity

if typing.TYPE_CHECKING:
    from py_moysklad.client import ApiClient


class IEndpoint(typing.Protocol):
    list: str
    retrieve: str
    create: str
    delete: str


class IEntityClientBase(typing.Protocol):
    @staticmethod
    @abstractmethod
    def entity_class() -> typing.Type[MetaEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_endpoint(self, endpoint: str) -> str:
        raise NotImplementedError()


class EntityClientBase(ABC, IEntityClientBase):
    def __init__(self, api: "ApiClient"):
        self.api = api


class BaseEndpoint(ABC, IEntityClientBase):
    @property
    def client(self):
        api = getattr(self, "api")
        if not api:
            raise Exception()  # FIXME: add custom exception
        return api.client


class GetByIdEndpoint(BaseEndpoint, ABC):
    def get(self, entity_id: str = None):
        if entity_id is None:
            response = self.client.get(endpoint=self.get_endpoint('list'))
            return ListEntity[self.entity_class()](**response)
        response = self.client.get(endpoint=self.get_endpoint('retrieve').format(id=entity_id))
        return self.entity_class()(**response)


class PostEndpoint(BaseEndpoint, ABC):
    def create(self, body: dict):
        response = self.client.post(endpoint=self.get_endpoint('create'), body=body)
        return self.entity_class()(**response)


class DeleteByIdEndpoint(BaseEndpoint, ABC):
    def delete(self, entity: typing.Union[MetaEntity, int]) -> None:
        if isinstance(entity, MetaEntity):
            entity_id = entity.id
        elif isinstance(entity, int):
            entity_id = entity
        else:
            raise Exception()

        return self.client.delete(endpoint=self.get_endpoint('delete').format(id=entity_id))


class ProductClient(EntityClientBase, GetByIdEndpoint, PostEndpoint, DeleteByIdEndpoint):
    endpoints = {
        'list': 'products',
        'create': 'products',
        'retrieve': 'products/{id}',
        'delete': 'products/{id}',
    }

    @staticmethod
    def entity_class() -> typing.Type[Product]:
        return Product

    def get_endpoint(self, endpoint: str) -> str:
        base_url = self.api.host.rstrip("/")
        new_value = str(self.endpoints[endpoint]).lstrip("/")
        return f"{base_url}/{new_value}"

