from dataclasses import dataclass
from decimal import Decimal

from py_moysklad.entities.price_type import PriceType


@dataclass
class Address:
    priceType: PriceType
    currency: Currency
    value: Decimal
