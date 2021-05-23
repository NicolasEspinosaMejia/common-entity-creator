from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer


Base = declarative_base()

class StudentByCourseModel(Base):

    __tablename__ = 'as_student_by_course'
    identifier_student_by_address = Column(Integer, primary_key=True)
    identifier_student = Column(Integer, ForeignKey('as_student'))
    identifier_address = Column(Integer, ForeignKey('as_student'))
