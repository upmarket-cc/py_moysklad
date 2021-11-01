from py_moysklad.entities.products.product import Product


def test_delete_from_string_uuid(client, mock_http_client):
    client.entity().product().delete("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.delete.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)


def test_delete_from_entity_id(client, mock_http_client, read_fixture):
    fixture = read_fixture("entities/product")

    product = Product(**fixture)
    client.entity().product().delete(product)

    mock_http_client.delete.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
