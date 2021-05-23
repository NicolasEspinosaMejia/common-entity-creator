from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CourseModel(Base):

    __tablename__ = 'as_course'
    identifier_course = Column(Integer(), primary_key=True)
    name_course = Column(String(), nullable=False, unique=True)
    course_start_date = Column(DateTime(), default=datetime.now())
    course_end_date = Column(DateTime(), nullable=False)
