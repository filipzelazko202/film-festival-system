from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base


class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    festival_id = Column(Integer, ForeignKey("festival.id"))