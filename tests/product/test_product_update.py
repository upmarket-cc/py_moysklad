from py_moysklad.entities.products.product import Product


def test_update_product(client, mock_http_client, read_fixture):
    mock_http_client.put.return_value = read_fixture("entities/product_update_response")

    product = Product(name="Мандарины", id="d950551c-2c7f-11e6-8a84-bae50000000b")
    product.name = "Мандарины777"
    client.entity().product().update(product)

    mock_http_client.put.assert_called_with(
        "localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b",
        data={"name": "Мандарины777", "id": "d950551c-2c7f-11e6-8a84-bae50000000b"},
        params=None,
    )
