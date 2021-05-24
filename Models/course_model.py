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

    def __init__(self,
                 name_course,
                 course_start_date,
                 course_end_date):
        self.name_course = name_course
        self.course_start_date = course_start_date
        self.course_end_date = course_end_date
