from sqlalchemy import Column, String, Integer, DateTime
from models.base import Base
from schemas import UserSchema


class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    join_date = Column(DateTime)

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name})"

    def to_schema(self):

        return UserSchema(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            join_date=self.join_date,
        )
