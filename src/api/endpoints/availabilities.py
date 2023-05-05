from typing import List
from fastapi import APIRouter, Depends
from api.dependencies import get_current_user, get_db

from schemas.availabilities import AddAvailabilityRange
from models.availability import AvailabilityInterval

router = APIRouter()


@router.get("/availability-ranges", response_model=List[AddAvailabilityRange])
async def get_availabilities(user=Depends(get_current_user)):
    ranges = [ai.to_schema() for ai in user.availability_intervals]
    print(ranges)
    return ranges


@router.post("/add-availability-range")
async def create_new_availability(
    availability_range: AddAvailabilityRange,
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    print(availability_range)
    availability = AvailabilityInterval.create(availability_range)
    availability.user = user
    db.add(availability)
    db.commit()
    return True
