from dataclasses import dataclass
from decimal import Decimal

from py_moysklad.entities.currency import Currency
from py_moysklad.entities.price_type import PriceType


@dataclass
class Price:
    priceType: PriceType
    currency: Currency
    value: Decimal
