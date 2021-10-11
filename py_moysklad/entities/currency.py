from dataclasses import dataclass
from decimal import Decimal

from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class Currency(MetaEntity):
    fullName: str
    rate: Decimal
    # private MultiplicityType multiplicity;
    # private UpdateType rateUpdateType;
    indirect: bool
    code: str
    isoCode: str
    system: bool
    # private Unit majorUnit;
    # private Unit minorUnit;
    archived: bool
