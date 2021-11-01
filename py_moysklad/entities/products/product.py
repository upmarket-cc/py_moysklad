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
from py_moysklad.responses.list_entity import ListEntity


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
    barcodes: Optional[List[Barcode]]


class Product(AbstractProduct):
    owner: Optional[Employee]
    shared: Optional[bool]
    group: Optional[Group]
    # sync_id: Optional[str]
    updated: Optional[datetime]
    external_code: Optional[str]
    archived: Optional[bool]
    path_name: Optional[str]
    images: Optional[ListEntity[Image]]
    supplier: Optional[Agent]
    attributes: Optional[List[Attribute]]
    # country: Optional[Country]
    article: Optional[str]
    tobacco: Optional[bool]
    weight: Optional[Decimal]
    volume: Optional[Decimal]
    packs: Optional[List[ProductPack]]
    alcoholic: Optional[AlcoholEntity]
    variants_count: Optional[int]
    is_serial_trackable: Optional[bool]
    weighed: Optional[bool]
    things: Optional[List[str]]
    # minimum_balance: Optional[Decimal]
    # ppe_type: Optional[str]
    # partial_disposal: Optional[bool]
    tracking_type: Optional[TrackingType]
    # tnved: Optional[str]
    # payment_item_type: Optional[GoodPaymentItemType]
    # tax_system: Optional[GoodTaxSystem]
