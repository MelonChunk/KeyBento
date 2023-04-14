from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

from models.base import Base


class Property(Base):

    __tablename__ = "property"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    city = Column(String)
    type = Column(String)
    country = Column(String)
    description = Column(String)
    address = Column(String)
    owner = relationship("User", back_populates="properties")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )

    def __repr__(self):
        return f"Property({self.id}, {self.city}, {self.country}, {self.description})"

    @classmethod
    def create(cls, schema):
        return cls(**schema.dict())
