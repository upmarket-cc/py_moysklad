from py_moysklad.entities.products.product import Product


def test_(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.rows[0].id == '26b36824-2c83-11e6-8a84-bae50000001b'


def test_2(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get('d950551c-2c7f-11e6-8a84-bae50000000b')

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.id == 'd950551c-2c7f-11e6-8a84-bae50000000b'


def test_3(client, mock_http_client, read_fixture):
    fixture = read_fixture("entities/product")
    mock_http_client.get.return_value = fixture

    product = Product(**fixture)
    got = client.entity().product().get(product.id)

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.id == 'd950551c-2c7f-11e6-8a84-bae50000000b'

