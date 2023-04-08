from typing import Optional

from datetime import datetime
from pydantic import BaseModel


class UserSchema(BaseModel):

    id: int
    username: str
    first_name: str
    last_name: str
    join_date: datetime
    last_seen: datetime
    about_me: Optional[str]
    avatar_url: Optional[str]


class CreateUserSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
