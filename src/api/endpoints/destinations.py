from fastapi import APIRouter, Request

from schemas.destinations import DestinationResponse, Destination
from schemas.pagination import Pagination

router = APIRouter()


destinations = [
    Destination(id=1, location="London"),
    Destination(id=2, location="New York"),
    Destination(id=3, location="Berlin"),
    Destination(id=4, location="Paris"),
    Destination(id=5, location="Edinburgh"),
    Destination(id=6, location="Newcastle"),
    Destination(id=7, location="Bern"),
]


@router.get("/destinations", response_model=DestinationResponse)
async def get_destinations(
    request: Request,
    limit: int = 3,
    offset: int = 0,
):  # pylint: disable=unused-argument

    to_send_destinations = destinations[offset:(offset + limit)]
    pagination = Pagination(
        count=len(to_send_destinations),
        offset=offset,
        limit=limit,
        total=len(destinations),
    )

    return DestinationResponse(destinations=to_send_destinations, pagination=pagination)


@router.get("/userdestinations/{username}", response_model=DestinationResponse)
async def get_destinations_for_user(
    request: Request,
    limit: int = 3,
    offset: int = 0,
):  # pylint: disable=unused-argument
    # TODO: make this user dependent
    to_send_destinations = destinations[offset:(offset + limit)]
    pagination = Pagination(
        count=len(to_send_destinations),
        offset=offset,
        limit=limit,
        total=len(destinations),
    )
    return DestinationResponse(destinations=to_send_destinations, pagination=pagination)
