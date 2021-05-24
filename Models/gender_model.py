from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GenderModel(Base):

    __tablename__ = 'as_gender'
    identifier_gender = Column(Integer, primary_key=True)
    name_gender = Column(String, nullable=False, unique=True)

    def __init__(self,
                 name_gender):
        self.name_gender = name_gender
