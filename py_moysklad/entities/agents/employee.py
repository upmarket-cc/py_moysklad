from typing import List

from datetime import datetime

from py_moysklad.entities.agents.agent import Agent
from py_moysklad.entities.attribute import Attribute
from py_moysklad.entities.cashier import Cashier
from py_moysklad.entities.group import Group
from py_moysklad.entities.image import Image


class Employee(Agent):
    owner: "Employee"
    shared: bool
    lastName: str
    externalCode: str
    shortFio: str
    created: datetime
    fullName: str
    archived: bool
    uid: str
    cashiers: List[Cashier]
    updated: datetime
    email: str
    group: Group
    description: str
    phone: str
    firstName: str
    middleName: str
    attributes: List[Attribute]
    image: Image
    inn: str
    position: str
