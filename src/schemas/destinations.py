from typing import List, Optional
from pydantic import BaseModel

from schemas.pagination import Pagination


class Destination(BaseModel):

    id: int
    location: str


class DestinationResponse(BaseModel):

    destinations: List[Destination]
    pagination: Optional[Pagination]
