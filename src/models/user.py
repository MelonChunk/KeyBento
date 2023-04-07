from sqlalchemy import Column, String, Integer, DateTime
from models.base import Base
from schemas import UserSchema, CreateUserSchema


class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    join_date = Column(DateTime)
    last_seen = Column(DateTime)
    about_me = Column(String)
    avatar_url = Column(String)

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name})"

    def to_schema(self):

        return UserSchema(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            join_date=self.join_date,
            username=self.username,
            last_seen=self.last_seen,
            about_me=self.about_me,
            avatar_url=self.avatar_url,
        )

    @classmethod
    def create(cls, user: CreateUserSchema):
        return cls(username=user.username, password=user.password, email=user.email)
