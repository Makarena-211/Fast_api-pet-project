import psycopg2 
from config import Base
from sqlalchemy import Column, Integer, String, Date

class Painting (Base):
    __tablename__ = 'paintings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    type = Column(String, nullable=False)























