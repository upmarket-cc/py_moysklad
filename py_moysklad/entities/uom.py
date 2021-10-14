from dataclasses import dataclass
from datetime import datetime

from py_moysklad.entities.agents.employee import Employee
from py_moysklad.entities.group import Group
from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class Uom(MetaEntity):
    updated: datetime
    description: str
    code: str
    externalCode: str
    shared: bool
    owner: Employee
    group: Group
