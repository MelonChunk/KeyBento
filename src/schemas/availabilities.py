from pydantic import BaseModel


class AddAvailabilityRange(BaseModel):
    startDate: str
    endDate: str
    key: str
