from sqlalchemy import Column, Integer, String
from database.db import Base
from sqlalchemy import Float

class Festival(Base):
    __tablename__ = "festival"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)