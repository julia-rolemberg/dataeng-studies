from src.models import db
from src.models.student import Student
from src.models.school_tests import SchoolTests
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 
import datetime

from src.services.course_service import get as get_course

def create(data):
    try:

        name = data.get('Name')
        if not name:
            json_abort(400,"name is required")

        course_id = data.get('CourseID')
        if not course_id:
            json_abort(400,"CourseID is required")

        age = data.get('Age')
        if not age:
            json_abort(400,"age is required")
        
        cpf = data.get('CPF')
        if not cpf:
            json_abort(400,"cpf is required")

        course = get_course(course_id)
 
        created = datetime.datetime.now()

        student = Student(Name=name, CourseID = course_id, Course=course, Created = created, Age = age, CPF = cpf)
        db.session.add(student)
        db.session.commit()


        return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        student = Student.query.filter_by(StudentID=id).first()

        if not student:
            json_abort(400,"Student not found")
        else:
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_all():
    try:
        
        student = Student.query.all()

        if not student:
            json_abort(400, "Student not found")
        else:
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error) 

def get_student_schoolTest(id):
    try:
        student = Student.query.filter_by(StudentID=id).first()
        student.listSchoolTests = SchoolTests.query.filter_by(StudentID=id).all()
        
        if not student:
            json_abort(400,"Student not found")
        else:
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        student = Student.query.filter_by(StudentID=id).first()

        if not student:
            json_abort(400,"student not found")
        else:

            name = data.get('Name')
            if not name:
                json_abort(400,"name is required")

            course_id = data.get('CourseID')
            if not course_id:
                json_abort(400,"CourseID is required")

            age = data.get('Age')
            if not age:
                json_abort(400,"age is required")
            
            cpf = data.get('CPF')
            if not cpf:
                json_abort(400,"cpf is required")


            student.Name = name
            student.CourseID = course_id
            student.Age = age
            student.CPF = cpf
            
            db.session.commit()
        
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        student = Student.query.filter_by(StudentID=id).first()

        if not student:
            json_abort(400,"Student not found")
        else:
            db.session.delete(student)
            db.session.commit()
        
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)