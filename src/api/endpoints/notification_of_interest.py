from fastapi import APIRouter, Depends
from schemas.notification_of_interest import NOISchema
from models import NotificationOfInterest

from api.exceptions import EmailAlreadyRegisteredException
from api.dependencies import get_db


router = APIRouter()


@router.post("/notification_of_interest")
async def register_interest(
    schema: NOISchema,
    db=Depends(get_db),
):

    noi = NotificationOfInterest.create(schema)

    try:
        db.add(noi)
        db.commit()

    except Exception as exc:
        raise EmailAlreadyRegisteredException from exc

    return True
