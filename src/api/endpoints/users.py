from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import func

from api.dependencies import get_db, get_settings
from api.endpoints.authentication import get_password_hash
from models import User
from schemas import UserSchema, CreateUserSchema

router = APIRouter()


@router.get("/create_user")
def create_test_user(settings=Depends(get_settings), db=Depends(get_db)):
    if settings.environment == "DEBUG":
        user = User(
            username="melonchunk",
            hashed_password=get_password_hash("password"),
            first_name="Melon",
            last_name="Chunk",
            join_date=datetime.now(),
            last_seen=datetime.now(),
            about_me="Looking for my dream vacation on melon island",
            avatar_url="https://i.imgur.com/oBPXx0D.png",
        )
        db.add(user)
        db.commit()


@router.post("/register_user")
def register_user(new_user: CreateUserSchema, db=Depends(get_db)):
    user = User.create(new_user)
    db.add(user)
    db.commit()


@router.get("/user/{username}", response_model=Optional[UserSchema])
def get_user(username: str, db=Depends(get_db)):
    user = db.query(User).filter(func.lower(User.username) == username.lower()).first()
    if user:
        user_response = user.to_schema()
    else:
        user_response = None
    return user_response
