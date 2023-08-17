from sqlalchemy import Column, Integer, String, UniqueConstraint

from models.base import Base


class NotificationOfInterest(Base):

    __tablename__ = "notification_of_interest"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    comment = Column(String)

    __table_args__ = (UniqueConstraint("email", name="interest_email_unique"),)

    def __repr__(self):
        return f"NotificationOfInterest({self.name}, {self.email})"

    @classmethod
    def create(cls, schema):
        return cls(**schema.dict())
