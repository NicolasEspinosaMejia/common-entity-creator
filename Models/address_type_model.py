from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AddressTypeModel(Base):

    __tablename__ = 'as_address_type'
    identifier_address_type = Column(Integer, primary_key=True)
    name_address_type = Column(String, nullable=False, unique=True)

    def __init__(self,
                 name_address_type):
        self.name_address_type = name_address_type
