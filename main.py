import json

from datetime import date
from sqlalchemy import Column, Integer, JSON, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.contexts.postgre_sql_context import PostgreSqlContext
from resources.utils.generals_utils import GeneralsUtils

index = 0
Base = declarative_base()
context =  PostgreSqlContext()

class AddressModel(Base):

    __tablename__ = 'as_address'
    identifier_address = Column(Integer, primary_key=True)
    permanent_address = Column(String, nullable=False, unique=True)
    type_address = Column(Integer)
    identifier_student = Column(Integer)
    student = Column(JSON)

    def __init__(self,
                 permanent_address,
                 type_address,
                 identifier_student,
                 student):
        self.permanent_address = permanent_address
        self.type_address = type_address
        self.identifier_student = identifier_student
        self.student = student

class AddressTypeModel(Base):

    __tablename__ = 'as_address_type'
    identifier_address_type = Column(Integer, primary_key=True)
    name_address_type = Column(String, nullable=False, unique=True)

    def __init__(self,
                 name_address_type):
        self.name_address_type = name_address_type

class CourseModel(Base):

    __tablename__ = 'as_course'
    identifier_course = Column(Integer(), primary_key=True)
    name_course = Column(String(), nullable=False, unique=True)
    course_start_date = Column(DateTime())
    course_end_date = Column(DateTime(), nullable=False)

    def __init__(self,
                 name_course,
                 course_start_date,
                 course_end_date):
        self.name_course = name_course
        self.course_start_date = course_start_date
        self.course_end_date = course_end_date

class GenderModel(Base):

    __tablename__ = 'as_gender'
    identifier_gender = Column(Integer, primary_key=True)
    name_gender = Column(String, nullable=False, unique=True)

    def __init__(self,
                 name_gender):
        self.name_gender = name_gender

class StudentModel(Base):

    __tablename__ = 'as_student'
    identifier_student = Column(Integer, primary_key=True)
    student_name = Column(String, nullable=False)
    student_last_name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    gender = Column(Integer)

    def __init__(self,
                 student_name,
                 student_last_name,
                 birth_date,
                 gender):
        self.student_name = student_name
        self.student_last_name = student_last_name
        self.birth_date = birth_date
        self.gender = gender

    def element_dict(self,
                     student_name,
                     student_last_name,
                     birth_date,
                     gender):
       return {"student_name": student_name,
               "student_last_name": student_last_name,
               "birth_date": birth_date,
               "gender": gender}

class StudentByAddressModel(Base):

    __tablename__ = 'as_student_by_address'
    identifier_student_by_address = Column(Integer, primary_key=True)
    identifier_student = Column(Integer)
    identifier_address = Column(Integer)

    def __init__(self,
                 identifier_student,
                 identifier_address):
        self.identifier_student = identifier_student
        self.identifier_address = identifier_address

class StudentByCourseModel(Base):

    __tablename__ = 'as_student_by_course'
    identifier_student_by_address = Column(Integer, primary_key=True)
    identifier_student = Column(Integer)
    identifier_course = Column(Integer)

    def __init__(self,
                 identifier_student,
                 identifier_course):
        self.identifier_student = identifier_student
        self.identifier_course = identifier_course

session = context.configure("POSTGRESQL_DB_SET_AS")

def database_structure_generic():

    home_address = AddressTypeModel("Home")
    office_address = AddressTypeModel("Office")
    temporary_address = AddressTypeModel("Temporary ")

    session.add(home_address)
    session.add(office_address)
    session.add(temporary_address)

    undefined = GenderModel("Undefined")
    male = GenderModel("Male")
    feminine = GenderModel("Feminine")

    session.add(undefined)
    session.add(male)
    session.add(feminine)

    session.commit()

def database_structure():

    get_gender = session.query(GenderModel).filter(
        GenderModel.name_gender == "Male"
    ).first()

    honorable_mention_student = StudentModel("Daniel Fernando",
                                             "Henao Zuñiga",
                                             date(2002,12,31).isoformat(),
                                             get_gender.identifier_gender)

    session.add(honorable_mention_student)

    student = (session.query(StudentModel).all())[index]
    student_structure = StudentModel.element_dict("student",
                                                  student.student_name,
                                                  student.student_last_name,
                                                  student.birth_date,
                                                  student.gender)

    get_type_address = session.query(AddressTypeModel).filter(
        AddressTypeModel.name_address_type == "Home"
    ).first()

    current_address = AddressModel("Cra 17a # 876D - 98B Caribean",
                                   get_type_address.identifier_address_type,
                                   student.identifier_student,
                                   student_structure)

    session.add(current_address)

    chemistry_course = CourseModel("Chemistry",
                              date(2021,1,1).isoformat(),
                              date(2021,6,15).isoformat())

    math_course = CourseModel("Math",
                              date(2021,1,1).isoformat(),
                              date(2021,6,15).isoformat())

    session.add(math_course)
    session.add(chemistry_course)

    student_course = session.query(StudentModel).filter(
        StudentModel.student_name.contains("Daniel")
    ).first()

    course_student_chemistry = session.query(CourseModel).filter(
        CourseModel.name_course == "Chemistry"
    ).first()

    course_student_math = session.query(CourseModel).filter(
        CourseModel.name_course == "Math"
    ).first()

    student_by_course_daniel = StudentByCourseModel(
        student_course.identifier_student,
        course_student_math.identifier_course)

    session.add(student_by_course_daniel)

    student_by_course_daniel = StudentByCourseModel(
        student_course.identifier_student,
        course_student_chemistry.identifier_course)

    session.add(student_by_course_daniel)

    home_address_student = StudentByAddressModel(
        current_address.identifier_student,
        current_address.identifier_address)

    session.add(home_address_student)

    session.commit()

if __name__ == "__main__":
    Base.metadata.drop_all(context.engine)
    Base.metadata.create_all(context.engine)
    database_structure_generic()
    database_structure()