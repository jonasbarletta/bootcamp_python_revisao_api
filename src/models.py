from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key = True, index = True) # chave primária
    name = Column(String, nullable = False)
    types = Column(String)
    weight = Column(Integer)
    created_at = Column(DateTime, default = func.now()) 
