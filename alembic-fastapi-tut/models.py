from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    author = Column(String)
    rating = Column(Integer)
    published = Column(Boolean)
