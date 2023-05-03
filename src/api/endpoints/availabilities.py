from fastapi import APIRouter, Depends
from api.dependencies import get_current_user, get_db

from schemas.availabilities import AddAvailabilityRange
from models.availability import AvailabilityInterval

router = APIRouter()


@router.post("/add-availability-range")
async def create_new_availability(
    availability_range: AddAvailabilityRange,
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    availability = AvailabilityInterval.create(availability_range)
    availability.user = user
    db.add(availability)
    db.commit()
    return True
