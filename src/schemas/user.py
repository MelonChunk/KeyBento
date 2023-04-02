from datetime import datetime
from pydantic import BaseModel


class UserSchema(BaseModel):

    id: int
    first_name: str
    last_name: str
    join_date: datetime
