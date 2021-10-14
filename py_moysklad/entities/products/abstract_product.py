from typing import List

from py_moysklad.entities.assortment import Assortment
from py_moysklad.entities.attached_file import AttachedFile
from py_moysklad.entities.barcode import Barcode
from py_moysklad.entities.price import Price
from py_moysklad.entities.product_folder import ProductFolder
from py_moysklad.entities.uom import Uom


class AbstractProduct(Assortment):
    code: str
    description: str
    vat: int
    effectiveVat: int
    productFolder: ProductFolder
    minPrice: Price
    buyPrice: Price
    salePrices: List[Price]
    uom: Uom
    barcodes: List[Barcode]
    files: List[AttachedFile]
