from py_moysklad.clients.generic import DeleteMixin, GenericEntityClient, RetrieveMixin, CreateMixin, UpdateMixin
from py_moysklad.entities.products.product import Product


class ProductClient(GenericEntityClient, RetrieveMixin, CreateMixin, UpdateMixin, DeleteMixin):
    endpoints = {
        "list": "products",
        "create": "products",
        "retrieve": "products/{id}",
        "update": "products/{id}",
        "delete": "products/{id}",
    }
    entity_class = Product
