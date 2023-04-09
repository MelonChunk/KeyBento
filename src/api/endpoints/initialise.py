from datetime import datetime
from typing import Any
from fastapi import APIRouter, Depends
from pydantic_factories import ModelFactory

from api.dependencies import get_db, get_settings
from api.dependencies.authentication import get_password_hash

from models import User, Property

from schemas.user import CreateUserSchema
from schemas.destinations import CreateProperty

router = APIRouter()


class UserFactory(ModelFactory[Any]):
    __model__ = CreateUserSchema


class PropertyFactory(ModelFactory[Any]):
    __model__ = CreateProperty


@router.get("/create_all")
def create_test_user(settings=Depends(get_settings), db=Depends(get_db)):
    if settings.environment == "DEBUG":
        melon = User(
            username="melonchunk",
            hashed_password=get_password_hash("password"),
            first_name="Melon",
            last_name="Chunk",
            join_date=datetime.now(),
            last_seen=datetime.now(),
            about_me="Looking for my dream vacation on melon island",
            avatar_url="https://i.imgur.com/oBPXx0D.png",
        )
        db.add(melon)
        db.commit()

        melons_props = PropertyFactory.batch(3)
        for prop in melons_props:
            prop = Property.create(prop)
            prop.owner = melon
            db.add(prop)
            db.commit()

        leroy = User(
            username="leroy",
            hashed_password=get_password_hash("password"),
            first_name="Leroy",
            last_name="Jenkins",
            join_date=datetime.now(),
            last_seen=datetime.now(),
            about_me="Looking for a place with dungeons",
            avatar_url="https://upload.wikimedia.org/wikipedia/en/d/da/Leeroy_Jenkins_WoW.webp",
        )
        db.add(leroy)
        db.commit()

        properties = PropertyFactory.batch(12)
        for prop in properties:
            user_schema = UserFactory.build()
            user = User.create(user_schema)
            db.add(user)
            db.commit()
            prop = Property.create(prop)
            prop.owner = user
            db.add(prop)
            db.commit()
