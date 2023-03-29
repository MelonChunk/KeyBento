from pydantic import BaseModel


class Destination(BaseModel):

    id: int
    location: str
