from dataclasses import dataclass


@dataclass
class Meta:
    href: str
    metadata_href: str
    type: str  # noqa: VNE003, FIXME: ENUM
    media_type: str
    uuid_href: str
    size: int
    limit: int
    offset: int
