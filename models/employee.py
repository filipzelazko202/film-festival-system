from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.db import Base

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    location_id = Column(Integer, ForeignKey("location.id"))