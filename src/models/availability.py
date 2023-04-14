from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship

from models.base import Base


class Availability(Base):

    __tablename__ = "availability"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    month = Column(String)
    available = Column(Boolean)

    user = relationship("User", back_populates="availabilities")

    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )

    def __repr__(self):
        return f"Availability({self.user.username},{self.month}, {self.available})"
