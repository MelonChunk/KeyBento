from datetime import datetime
from random import choice
from typing import Any
from fastapi import APIRouter, Depends
from pydantic_factories import ModelFactory


from api.dependencies import get_db, get_settings
from api.dependencies.authentication import get_password_hash

from data_processing.sample_data import load_users

from models import User, Property

from schemas.user import CreateUserSchema
from schemas.destinations import CreateProperty

router = APIRouter()


class UserFactory(ModelFactory[Any]):
    __model__ = CreateUserSchema


class PropertyFactory(ModelFactory[Any]):
    __model__ = CreateProperty


city_countries = [
    ("Berlin", "Germany"),
    ("New York", "USA"),
    ("London", "England"),
    ("Wellington", "New Zealand"),
    ("Madrid", "Spain"),
    ("Paris", "France"),
]
descriptions = [
    "Nice and cosy place",
    "In the middle of the city",
    "Lots of restaurants",
    "Close to the zoo",
]
usernames = ["Dick", "Tom", "Harry"]


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

        for _ in range(3):
            city_country = choice(city_countries)
            description = choice(descriptions)
            prop = PropertyFactory.build(
                type=choice(["Flat", "House"]),
                city=city_country[0],
                country=city_country[1],
                description=description,
            )
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

        for prop in range(12):

            user_schema = UserFactory.build(username=choice(usernames))
            user = User.create(user_schema)
            db.add(user)
            db.commit()
            city_country = choice(city_countries)
            description = choice(descriptions)
            prop = PropertyFactory.build(
                type=choice(["Flat", "House"]),
                city=city_country[0],
                country=city_country[1],
                description=description,
            )
            prop = Property.create(prop)
            prop.owner = user
            db.add(prop)
            db.commit()


@router.get("/create_sample_users")
def create_sample_users(settings=Depends(get_settings), db=Depends(get_db)):
    if settings.environment == "DEBUG":
        load_users(db)
        melon = User(
            username="melonchunk",
            hashed_password=get_password_hash("password"),
            first_name="Melon",
            last_name="Chunk",
            last_seen=datetime.now(),
            about_me="Looking for my dream vacation on melon island",
            avatar_url="https://i.imgur.com/oBPXx0D.png",
        )
        db.add(melon)
        db.commit()
