import psycopg2 
from config import Base
from sqlalchemy import Column, Integer, String, Date
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import UUIDType

class Painting (Base):
    __tablename__ = 'paintings'
    #id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    type = Column(String, nullable=False)























