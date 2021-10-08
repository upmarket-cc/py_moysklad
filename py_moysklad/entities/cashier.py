from dataclasses import dataclass

from py_moysklad.entities.agents.employee import Employee
from py_moysklad.entities.meta_entity import MetaEntity


@dataclass
class Cashier(MetaEntity):
    employee: Employee
    # private RetailStore retailStore;
