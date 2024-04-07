import psycopg2 
from config import Base
from sqlalchemy import Column, Integer, String, Date

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    role = Column(String, nullable=False)
