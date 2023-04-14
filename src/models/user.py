from datetime import datetime
import urllib
import hashlib

from sqlalchemy import Column, String, Integer, DateTime, Boolean, func
from sqlalchemy.orm import relationship

from models.base import Base
from schemas import UserSchema, CreateUserSchema


class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    last_seen = Column(DateTime)
    phone_number = Column(String)
    about_me = Column(String)
    avatar_url = Column(String)
    disabled = Column(Boolean, default=False)

    properties = relationship("Property", uselist=True)
    availabilities = relationship("Availability", uselist=True)
    city_interests = relationship("CityInterest", uselist=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name})"

    def to_schema(self):

        return UserSchema(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            last_seen=self.last_seen,
            join_date=self.created_at,
            about_me=self.about_me,
            avatar_url=self.avatar_url,
        )

    @staticmethod
    def generate_gravatar_url(email):
        size = 40
        gravatar_url = (
            "https://www.gravatar.com/avatar/"
            + hashlib.md5(email.lower().encode("utf-8")).hexdigest()
            + "?"
        )
        gravatar_url += urllib.parse.urlencode({"s": str(size)})
        return gravatar_url

    @classmethod
    def create(cls, user: CreateUserSchema):
        from api.dependencies.authentication import get_password_hash

        return cls(
            username=user.username,
            hashed_password=get_password_hash(user.password),
            email=user.email,
            avatar_url=cls.generate_gravatar_url(user.email),
            last_seen=datetime.now(),
            first_name=user.first_name,
            last_name=user.last_name,
        )
