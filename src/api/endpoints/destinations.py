from typing import List
from fastapi import APIRouter, Request

from schemas.destinations import Destination

router = APIRouter()


@router.get("/destinations", response_model=List[Destination])
async def get_destinations(
    request: Request,
):  # pylint: disable=unused-argument

    destinations = [
        Destination(id=1, location="London"),
        Destination(id=2, location="New York"),
        Destination(id=3, location="Berlin"),
        Destination(id=4, location="Paris"),
    ]
    return destinations
