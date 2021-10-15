from typing import Optional

from pydantic import BaseModel


class Meta(BaseModel):
    href: str
    metadataHref: str
    type: str  # noqa: VNE003, FIXME: ENUM
    mediaType: Optional[str]
    uuidHref: Optional[str]
    size: Optional[int]
    limit: Optional[int]
    offset: Optional[int]
