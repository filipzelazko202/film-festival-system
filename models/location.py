from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.db import Base


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    festival_id = Column(Integer, ForeignKey("festival.id"))