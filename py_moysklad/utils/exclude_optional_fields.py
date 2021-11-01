from pydantic import BaseModel


def _union(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            _union(value, node)
        else:
            destination[key] = value

    return destination


def exclude_optional_dict(model: BaseModel):
    return _union(model.dict(exclude_unset=True), model.dict(exclude_none=True))
