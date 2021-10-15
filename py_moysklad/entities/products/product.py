from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from py_moysklad.entities.agents.agent import Agent
from py_moysklad.entities.agents.employee import Employee
from py_moysklad.entities.attribute import Attribute
from py_moysklad.entities.barcode import Barcode
from py_moysklad.entities.country import Country
from py_moysklad.entities.group import Group
from py_moysklad.entities.image import Image
from py_moysklad.entities.products.abstract_product import AbstractProduct
from py_moysklad.entities.products.good_payment_item_type import GoodPaymentItemType
from py_moysklad.entities.products.good_tax_system import GoodTaxSystem
from py_moysklad.entities.uom import Uom


class TrackingType(Enum):
    NOT_TRACKED = "NOT_TRACKED"
    TOBACCO = "TOBACCO"
    SHOES = "SHOES"
    LP_CLOTHES = "LP_CLOTHES"
    LP_LINENS = "LP_LINENS"
    PERFUMERY = "PERFUMERY"
    ELECTRONICS = "ELECTRONICS"
    TIRES = "TIRES"
    OTP = "OTP"


class AlcoholEntity(BaseModel):
    excise: bool
    type: int
    strength: Decimal
    volume: Decimal


class ProductPack(BaseModel):
    id: str
    uom: Uom
    quantity: Decimal
    barcodes: List[Barcode]


class Product(AbstractProduct):
    # owner: Employee
    # shared: bool
    group: Group
    # syncId: str
    # updated: datetime
    # externalCode: str
    # archived: bool
    # pathName: str
    # images: List[Image]
    # supplier: Agent
    # attributes: List[Attribute]
    # country: Country
    # article: str
    # tobacco: bool
    # weight: Decimal
    # volume: Decimal
    # packs: List[ProductPack]
    # alcoholic: AlcoholEntity
    # variantsCount: int
    # isSerialTrackable: bool
    # weighed: bool
    # things: List[str]
    # minimumBalance: Decimal
    # ppeType: str
    # partialDisposal: bool
    # trackingType: TrackingType
    # tnved: str
    # paymentItemType: GoodPaymentItemType
    # taxSystem: GoodTaxSystem
