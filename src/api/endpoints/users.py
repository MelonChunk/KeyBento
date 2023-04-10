from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import func

from api.dependencies import get_db, get_current_user

from models import User
from schemas import UserSchema

router = APIRouter()


@router.get("/user/{username}", response_model=Optional[UserSchema])
def get_user_by_name(username: str, db=Depends(get_db)):
    user = db.query(User).filter(func.lower(User.username) == username.lower()).first()
    if user:
        return user.to_schema()
    return None


@router.get("/me", response_model=Optional[UserSchema])
def get_user(user=Depends(get_current_user)):
    if user:
        user_response = user.to_schema()
    else:
        user_response = None
    return user_response
