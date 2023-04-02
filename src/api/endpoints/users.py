from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends

from api.dependencies import get_db, get_settings
from models import User
from schemas import UserSchema

router = APIRouter()


@router.get("/create_user")
def create_test_user(settings=Depends(get_settings), db=Depends(get_db)):
    if settings.environment == "DEBUG":
        user = User(first_name="Melon", last_name="Chunk", join_date=datetime.now())
        db.add(user)
        db.commit()


@router.get("/user/{user_id}", response_model=Optional[UserSchema])
def get_user(user_id, db=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user_response = user.to_schema()
    else:
        user_response = None
    return user_response
