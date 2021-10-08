from dataclasses import dataclass
from datetime import datetime

from py_moysklad.entities.agents.employee import Employee
from py_moysklad.entities.attachment import Attachment


@dataclass
class AttachedFile(Attachment):
    created: datetime
    createdBy: Employee
