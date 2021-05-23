from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()

class AddressModel(Base):

    __tablename__ = 'as_address'
    identifier_address = Column(Integer, primary_key=True)
    permanent_address = Column(String, nullable=False, unique=True)
    type_address = Column(Integer, ForeignKey('as_address_type'))
    identifier_student = Column(Integer)
    student = Column(JSON, nullable=False, unique=True)
