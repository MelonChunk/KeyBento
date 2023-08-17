from pydantic import BaseModel


class NOISchema(BaseModel):

    email: str
    name: str
    comment: str
