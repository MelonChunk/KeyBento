from datetime import datetime
from pydantic import BaseModel


class UserSchema(BaseModel):

    id: int
    username: str
    first_name: str
    last_name: str
    join_date: datetime
    last_seen: datetime
    about_me: str
    avatar_url: str


class CreateUserSchema(BaseModel):
    username: str
    email: str
    password: str
