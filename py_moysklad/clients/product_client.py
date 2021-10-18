from py_moysklad.clients.generic import DeleteByIdEndpoint, EntityClientBase, GetByIdEndpoint, PostEndpoint
from py_moysklad.entities.products.product import Product


class ProductClient(EntityClientBase, GetByIdEndpoint, PostEndpoint, DeleteByIdEndpoint):
    endpoints = {
        "list": "products",
        "create": "products",
        "retrieve": "products/{id}",
        "delete": "products/{id}",
    }
    entity_class = Product
