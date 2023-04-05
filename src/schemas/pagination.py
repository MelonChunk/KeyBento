from pydantic import BaseModel


class Pagination(BaseModel):

    count: int
    limit: int
    offset: int
    total: int
