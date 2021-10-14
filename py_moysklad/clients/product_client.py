import typing
from abc import ABC, abstractmethod

from apiclient import endpoint

from py_moysklad.entities.meta_entity import MetaEntity
from py_moysklad.entities.products.product import Product

if typing.TYPE_CHECKING:
    from py_moysklad.client import ApiClient


class IEndpoint(typing.Protocol):
    list: str
    retrieve: str
    create: str
    delete: str


@endpoint(base_url="https://jsonplaceholder.typicode.com")
class Endpoint(IEndpoint):
    list = "todos"
    create = "todos"
    retrieve = "todos/{id}"
    delete = "todos/{id}"


class IEntityClientBase(typing.Protocol):
    @staticmethod
    @abstractmethod
    def entity_class() -> typing.Type[MetaEntity]:
        raise NotImplementedError()


class EntityClientBase(ABC, IEntityClientBase):
    def __init__(self, api: "ApiClient"):
        self.api = api


class BaseEndpoint(ABC):
    @property
    def client(self):
        api = getattr(self, "api")
        if not api:
            raise Exception()  # FIXME: add custom exception
        return api.client


class GetByIdEndpoint(BaseEndpoint):
    endpoints: IEndpoint

    def get(self, entity_id: str = None):
        _endpoint = self.endpoints.list if entity_id is None else self.endpoints.retrieve.format(id=entity_id)
        return self.client.get(endpoint=_endpoint)


class PostEndpoint(BaseEndpoint):
    endpoints: IEndpoint

    def create(self, body: dict):
        return self.client.get(endpoint=self.endpoints.create, body=body)


class DeleteByIdEndpoint(BaseEndpoint):
    endpoints: IEndpoint

    def delete(self, entity: typing.Union[MetaEntity, int]) -> None:
        if isinstance(entity, MetaEntity):
            entity_id = entity.id
        elif isinstance(entity, int):
            entity_id = entity
        else:
            raise Exception()

        return self.client.delete(endpoint=self.endpoints.delete.format(id=entity_id))


class ProductClient(EntityClientBase, GetByIdEndpoint, PostEndpoint, DeleteByIdEndpoint):
    endpoints = Endpoint

    @staticmethod
    def entity_class() -> typing.Type[Product]:
        return Product
