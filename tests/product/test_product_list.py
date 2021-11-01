from datetime import datetime
from decimal import Decimal


def test_serialize_metadata(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.meta.href == "https://online.moysklad.ru/api/remap/1.2/entity/product/"
    assert got.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata"
    assert got.meta.type == "product"
    assert got.meta.size == 5
    assert got.meta.limit == 1000
    assert got.meta.offset == 0


def test_serialize_context(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.context.employee.meta.href == "https://online.moysklad.ru/api/remap/1.2/context/employee"
    assert (
        got.context.employee.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/employee/metadata"
    )
    assert got.context.employee.meta.type == "employee"
    assert got.context.employee.meta.media_type == "application/json"


def test_serialize_list_of_products_2(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/product/26b36824-2c83-11e6-8a84-bae50000001b"
    )
    assert got.rows[0].meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata"
    assert got.rows[0].meta.type == "product"
    assert got.rows[0].meta.media_type == "application/json"
    assert got.rows[0].id == "26b36824-2c83-11e6-8a84-bae50000001b"
    assert got.rows[0].account_id == "6270cd18-2c7f-11e6-8a84-bae500000001"
    assert got.rows[0].shared is False
    assert got.rows[0].archived is False
    assert got.rows[0].updated == datetime(2016, 6, 7, 10, 40, 48)
    assert got.rows[0].name == "Тыква"
    assert got.rows[0].description == "Тыква, Германия"
    assert got.rows[0].code == "pumpkin1"
    assert got.rows[0].external_code == "456pumpkin"
    assert got.rows[0].path_name == ""
    assert got.rows[0].vat == 18
    # assert got.rows[0].vat_enabled is True  # dont have
    assert got.rows[0].effective_vat == 18
    # assert got.rows[0].use_parent_vat is False  # dont have
    # assert got.rows[0].effective_vat_enabled is True  # dont have
    # assert got.rows[0].discount_prohibited is True  # dont have
    assert got.rows[0].article == "Ar23"
    assert got.rows[0].weight == Decimal("200")
    assert got.rows[0].volume == Decimal("300")
    assert got.rows[0].variants_count == 0


def test_serialize_owner(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].owner.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/employee/faba7f37-2e58-11e6-8a84-bae500000028"
    )
    assert got.rows[0].owner.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/employee/metadata"
    assert got.rows[0].owner.meta.type == "employee"
    assert got.rows[0].owner.meta.media_type == "application/json"


def test_serialize_group(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].group.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/group/f97aa1fb-2e58-11e6-8a84-bae500000002"
    )
    assert got.rows[0].group.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/group/metadata"
    assert got.rows[0].group.meta.type == "group"
    assert got.rows[0].group.meta.media_type == "application/json"


def test_serialize_uom(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].uom.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/uom/19f1edc0-fc42-4001-94cb-c9ec9c62ec10"
    )
    assert got.rows[0].uom.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/uom/metadata"
    assert got.rows[0].uom.meta.type == "uom"
    assert got.rows[0].uom.meta.media_type == "application/json"


def test_serialize_supplier(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].supplier.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/counterparty/6313d1e7-2c7f-11e6-8a84-bae500000051"
    )
    assert (
        got.rows[0].supplier.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/counterparty/metadata"
    )
    assert got.rows[0].supplier.meta.type == "counterparty"
    assert got.rows[0].supplier.meta.media_type == "application/json"


def test_serialize_attributes(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].attributes[0].meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata/attributes/0c2e54cd-2c80-11e6-8a84-bae50000009c"
    )
    assert got.rows[0].attributes[0].meta.type == "attributemetadata"
    assert got.rows[0].attributes[0].meta.media_type == "application/json"
    assert got.rows[0].attributes[0].id == "0c2e54cd-2c80-11e6-8a84-bae50000009c"
    assert got.rows[0].attributes[0].name == "Экспорт"
    assert got.rows[0].attributes[0].type.value == "boolean"
    assert got.rows[0].attributes[0].value is True


def test_serialize_min_price(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.rows[0].min_price.value == 500
    assert (
        got.rows[0].min_price.currency.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/10772c12-36e7-11e7-8a7f-40d000000097"
    )
    assert (
        got.rows[0].min_price.currency.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/metadata"
    )
    assert got.rows[0].min_price.currency.meta.type == "currency"
    assert got.rows[0].min_price.currency.meta.media_type == "application/json"


def test_serialize_buy_price(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.rows[0].buy_price.value == 54
    assert (
        got.rows[0].buy_price.currency.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/6314188d-2c7f-11e6-8a84-bae500000055"
    )
    assert (
        got.rows[0].buy_price.currency.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/metadata"
    )
    assert got.rows[0].buy_price.currency.meta.type == "currency"
    assert got.rows[0].buy_price.currency.meta.media_type == "application/json"


def test_serialize_sale_prices(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.rows[0].sale_prices[0].value == 3353
    assert got.rows[0].sale_prices[0].price_type.id == "672559f1-cbf3-11e1-9eb9-889ffa6f49fd"
    assert got.rows[0].sale_prices[0].price_type.name == "Цена продажи"
    assert got.rows[0].sale_prices[0].price_type.external_code == "cbcf493b-55bc-11d9-848a-00112f43529a"
    assert (
        got.rows[0].sale_prices[0].price_type.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/context/companysettings/pricetype/672559f1-cbf3-11e1-9eb9-889ffa6f49fd"
    )
    assert got.rows[0].sale_prices[0].price_type.meta.type == "pricetype"
    assert got.rows[0].sale_prices[0].price_type.meta.media_type == "application/json"
    assert (
        got.rows[0].sale_prices[0].currency.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/6314188d-2c7f-11e6-8a84-bae500000055"
    )
    assert (
        got.rows[0].sale_prices[0].currency.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/metadata"
    )
    assert got.rows[0].sale_prices[0].currency.meta.type == "currency"
    assert got.rows[0].sale_prices[0].currency.meta.media_type == "application/json"


def test_serialize_images(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert (
        got.rows[0].images.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/product/26b36824-2c83-11e6-8a84-bae50000001b/images"
    )
    assert got.rows[0].images.meta.type == "image"
    assert got.rows[0].images.meta.media_type == "application/json"


def test_serialize_barcodes(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product_list")

    got = client.entity().product().get()

    mock_http_client.get.assert_called_with("localhost/products", params=None)
    assert got.rows[0].barcodes[0].type.value == "EAN8"
    assert got.rows[0].barcodes[0].value == "20000000"
