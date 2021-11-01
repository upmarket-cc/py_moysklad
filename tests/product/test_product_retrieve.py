from datetime import datetime
from decimal import Decimal

from py_moysklad.entities.products.product import Product


def test_serialize_metadata(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.meta.href == "https://online.moysklad.ru/api/remap/1.2/entity/product/d950551c-2c7f-11e6-8a84-bae50000000b"
    assert got.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata"
    assert got.meta.type == "product"
    assert got.meta.size is None
    assert got.meta.limit is None
    assert got.meta.offset is None


def test_serialize_list_of_products_2(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/product/d950551c-2c7f-11e6-8a84-bae50000000b"
    )
    assert got.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata"
    assert got.meta.type == "product"
    assert got.meta.media_type == "application/json"
    assert got.id == "d950551c-2c7f-11e6-8a84-bae50000000b"
    assert got.account_id == "6270cd18-2c7f-11e6-8a84-bae500000001"
    assert got.shared is False
    assert got.archived is False
    assert got.updated == datetime(2016, 6, 7, 10, 45, 16)
    assert got.name == "Бананы"
    assert got.description == "Бананы, Африка"
    assert got.code == "one1"
    assert got.external_code == "456"
    assert got.path_name == ""
    assert got.vat == 18
    # assert got.vat_enabled is True  # dont have
    assert got.effective_vat == 18
    # assert got.use_parent_vat is False  # dont have
    # assert got.effective_vat_enabled is True  # dont have
    # assert got.discount_prohibited is True  # dont have
    assert got.article == "Ar23"
    assert got.weight == Decimal("200")
    assert got.volume == Decimal("300")
    assert got.variants_count == 0
    assert got.is_serial_trackable is True
    assert got.tracking_type.value == 'NOT_TRACKED'
    assert got.things[0] == 'F564X056'
    assert got.weighed is None
    assert got.tobacco is None


def test_serialize_owner(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.owner.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/employee/faba7f37-2e58-11e6-8a84-bae500000028"
    )
    assert got.owner.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/employee/metadata"
    assert got.owner.meta.type == "employee"
    assert got.owner.meta.media_type == "application/json"


def test_serialize_group(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.group.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/group/f97aa1fb-2e58-11e6-8a84-bae500000002"
    )
    assert got.group.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/group/metadata"
    assert got.group.meta.type == "group"
    assert got.group.meta.media_type == "application/json"


def test_serialize_packs(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.packs[0].id == "c6bdee6f-2c83-11e6-8a84-bae5000000a4"
    assert got.packs[0].quantity == 35
    assert (
            got.packs[0].uom.meta.href
            == "https://online.moysklad.ru/api/remap/1.2/entity/uom/c6b91d63-2c83-11e6-8a84-bae5000000a1"
    )
    assert got.packs[0].uom.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/uom/metadata"
    assert got.packs[0].uom.meta.type == "uom"
    assert got.packs[0].uom.meta.media_type == "application/json"


def test_serialize_uom(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.uom.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/uom/19f1edc0-fc42-4001-94cb-c9ec9c62ec10"
    )
    assert got.uom.meta.metadata_href == "https://online.moysklad.ru/api/remap/1.2/entity/uom/metadata"
    assert got.uom.meta.type == "uom"
    assert got.uom.meta.media_type == "application/json"


def test_serialize_supplier(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.supplier.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/counterparty/6313d1e7-2c7f-11e6-8a84-bae500000051"
    )
    assert (
        got.supplier.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/counterparty/metadata"
    )
    assert got.supplier.meta.type == "counterparty"
    assert got.supplier.meta.media_type == "application/json"


def test_serialize_attributes(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.attributes[0].meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata/attributes/0c2e54cd-2c80-11e6-8a84-bae50000009c"
    )
    assert got.attributes[0].meta.type == "attributemetadata"
    assert got.attributes[0].meta.media_type == "application/json"
    assert got.attributes[0].id == "0c2e54cd-2c80-11e6-8a84-bae50000009c"
    assert got.attributes[0].name == "Экспорт"
    assert got.attributes[0].type.value == "boolean"
    assert got.attributes[0].value is False


def test_serialize_min_price(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.min_price.value == 532000
    assert (
        got.min_price.currency.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/10772c12-36e7-11e7-8a7f-40d000000097"
    )
    assert (
        got.min_price.currency.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/metadata"
    )
    assert got.min_price.currency.meta.type == "currency"
    assert got.min_price.currency.meta.media_type == "application/json"


def test_serialize_buy_price(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.buy_price.value == 23553000
    assert (
        got.buy_price.currency.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/6314188d-2c7f-11e6-8a84-bae500000055"
    )
    assert (
        got.buy_price.currency.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/metadata"
    )
    assert got.buy_price.currency.meta.type == "currency"
    assert got.buy_price.currency.meta.media_type == "application/json"


def test_serialize_sale_prices(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.sale_prices[0].value == 346347237000
    assert got.sale_prices[0].price_type.id == "672559f1-cbf3-11e1-9eb9-889ffa6f49fd"
    assert got.sale_prices[0].price_type.name == "Цена продажи"
    assert got.sale_prices[0].price_type.external_code == "cbcf493b-55bc-11d9-848a-00112f43529a"
    assert (
        got.sale_prices[0].price_type.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/context/companysettings/pricetype/672559f1-cbf3-11e1-9eb9-889ffa6f49fd"
    )
    assert got.sale_prices[0].price_type.meta.type == "pricetype"
    assert got.sale_prices[0].price_type.meta.media_type == "application/json"
    assert (
        got.sale_prices[0].currency.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/6314188d-2c7f-11e6-8a84-bae500000055"
    )
    assert (
        got.sale_prices[0].currency.meta.metadata_href
        == "https://online.moysklad.ru/api/remap/1.2/entity/currency/metadata"
    )
    assert got.sale_prices[0].currency.meta.type == "currency"
    assert got.sale_prices[0].currency.meta.media_type == "application/json"


def test_serialize_images(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert (
        got.images.meta.href
        == "https://online.moysklad.ru/api/remap/1.2/entity/product/d950551c-2c7f-11e6-8a84-bae50000000b/images"
    )
    assert got.images.meta.type == "image"
    assert got.images.meta.media_type == "application/json"


def test_serialize_barcodes(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.barcodes[0].type.value == "EAN8"
    assert got.barcodes[0].value == "20000000"


def test_get_from_string_uuid(client, mock_http_client, read_fixture):
    mock_http_client.get.return_value = read_fixture("entities/product")

    got = client.entity().product().get("d950551c-2c7f-11e6-8a84-bae50000000b")

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.id == "d950551c-2c7f-11e6-8a84-bae50000000b"


def test_get_from_entity_id(client, mock_http_client, read_fixture):
    fixture = read_fixture("entities/product")
    mock_http_client.get.return_value = fixture

    product = Product(**fixture)
    got = client.entity().product().get(product)

    mock_http_client.get.assert_called_with("localhost/products/d950551c-2c7f-11e6-8a84-bae50000000b", params=None)
    assert got.id == "d950551c-2c7f-11e6-8a84-bae50000000b"
