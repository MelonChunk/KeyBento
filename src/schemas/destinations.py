from typing import List, Optional
from pydantic import BaseModel

from schemas.pagination import Pagination
from schemas.user import UserSchema


class Destination(BaseModel):

    id: int
    city: str
    country: str
    description: str
    type: str
    address: str
    owner: Optional[UserSchema]

    @classmethod
    def from_db_obj(cls, obj):
        owner = obj.owner.to_schema()
        return cls(
            id=obj.id,
            city=obj.city,
            country=obj.country,
            description=obj.description,
            type=obj.type,
            address=obj.address,
            owner=owner
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
