from pydantic.generics import GenericModel


class Entity(GenericModel):
    class Config:
        arbitrary_types_allowed = True

