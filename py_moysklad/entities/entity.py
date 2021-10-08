import copy
from abc import ABC


class Entity(ABC):
    @classmethod
    def clone(cls, original: "Entity") -> "Entity":
        return copy.deepcopy(original)
