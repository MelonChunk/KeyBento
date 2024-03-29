from fastapi import APIRouter, Depends

from sqlalchemy import desc

from schemas.destinations import DestinationResponse, Destination, CreateProperty, removeProperty
from schemas.pagination import Pagination
from models.user import User
from models.properties import Property
from api.dependencies import get_current_user, get_db

router = APIRouter()


@router.get("/destinations", response_model=DestinationResponse)
async def get_destinations(
    limit: int = 3, offset: int = 0, db=Depends(get_db), user=Depends(get_current_user)
):   # pylint: disable=unused-argument

    destinations = (
        db.query(Property)
        .filter(Property.owner_id != user.id)
        .order_by(desc(Property.updated_at))
        .all()
    )
    destinations = [Destination.from_db_obj(des) for des in destinations]
    to_send_destinations = destinations[offset: (offset + limit)]
    pagination = Pagination(
        count=len(to_send_destinations),
        offset=offset,
        limit=limit,
        total=len(destinations),
    )

    return DestinationResponse(destinations=to_send_destinations, pagination=pagination)


@router.get("/userdestinations/{username}", response_model=DestinationResponse)
async def get_destinations_for_user(
    username: str,
    limit: int = 3,
    offset: int = 0,
    db=Depends(get_db),
):
    user = db.query(User).filter(User.username == username).first()
    if user:
        destinations = [Destination.from_db_obj(des) for des in user.properties]
        to_send_destinations = destinations[offset: (offset + limit)]
    else:
        destinations = []
        to_send_destinations = []
    pagination = Pagination(
        count=len(to_send_destinations),
        offset=offset,
        limit=limit,
        total=len(destinations),
    )

    return DestinationResponse(destinations=to_send_destinations, pagination=pagination)


@router.post("/new_property", response_model=Destination)
async def create_new_property(
    new_property: CreateProperty, user=Depends(get_current_user), db=Depends(get_db)
):
    property = Property.create(new_property)  # pylint: disable=(redefined-builtin)
    property.owner = user
    db.add(property)
    db.commit()
    return Destination.from_db_obj(property)


@router.post("/remove_property")
async def delete_property(
    remove_property: removeProperty, db=Depends(get_db)
):
    db.query(Property).filter(Property.id == remove_property.id).delete()
    db.commit()
    return True
