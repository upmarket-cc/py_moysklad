from dataclasses import dataclass
from datetime import datetime

from py_moysklad.entities.attached_file import AttachedFile


@dataclass
class Image(AttachedFile):
    updated: datetime
