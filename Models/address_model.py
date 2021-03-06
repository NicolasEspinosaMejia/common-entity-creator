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

    def __init__(self,
                 permanent_address,
                 type_address,
                 identifier_student,
                 student):
        self.permanent_address = permanent_address
        self.type_address = type_address
        self.identifier_student = identifier_student
        self.student = student
