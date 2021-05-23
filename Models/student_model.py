from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, JSON, String, DateTime


Base = declarative_base()

class StudentModel(Base):

    __tablename__ = 'as_student'
    identifier_student = Column(Integer, primary_key=True)
    student_name = Column(String, nullable=False)
    student_last_name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    gender = Column(String, ForeignKey('as_gender'))
