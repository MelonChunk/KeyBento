from typing import List, Optional
from pydantic import BaseModel

from schemas.pagination import Pagination


class Destination(BaseModel):

    id: int
    city: str
    country: str
    description: str
    type: str
    address: str

    @classmethod
    def from_db_obj(cls, obj):
        return cls(
            id=obj.id,
            city=obj.city,
            country=obj.country,
            description=obj.description,
            type=obj.type,
            address=obj.address,
        )


class DestinationResponse(BaseModel):

    destinations: List[Destination]
    pagination: Optional[Pagination]


class CreateProperty(BaseModel):

    city: str
    country: str
    description: str
    type: str
    address: str
