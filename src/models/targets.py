from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship

from models.base import Base


class CityInterest(Base):

    __tablename__ = "city_interest"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    city = Column(String)
    interested = Column(Boolean)

    user = relationship("User", back_populates="city_interests")

    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )

    def __repr__(self):
        return f"CityInterest({self.user.username},{self.city}, {self.interested})"
