from py_moysklad.entities.products.product import Product


def test_create_product(client, mock_http_client, read_fixture):
    mock_http_client.post.return_value = read_fixture("entities/product_create_response")

    new_product = Product(name="Мандарины")
    client.entity().product().create(new_product)

    mock_http_client.post.assert_called_with("localhost/products", data={"name": "Мандарины"}, params=None)
