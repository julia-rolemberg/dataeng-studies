from src.models import db
from src.models.school_tests import SchoolTests
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime


from src.services.student_service import get as get_student


def create(data):
    try:

        title = data.get('Title')
        if not title:
            json_abort(400,"title is required")

        student_id = data.get('StudentID')
        if not student_id:
            json_abort(400,"StudentID is required")

        test_grade = data.get('TestGrade')
        if not test_grade:
            json_abort(400,"test_grade is required")

        concept = data.get('Concept')
        if not concept:
            json_abort(400,"concept is required")

        student = get_student(student_id)
 
        created = datetime.datetime.now()

        school_tests = SchoolTests(Title=title,StudentID=student_id, Student=student, TestGrade=test_grade,Created=created, Concept=concept)
        db.session.add(school_tests)
        db.session.commit()

        return school_tests

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        school_tests = SchoolTests.query.filter_by(SchoolTestsID=id).first()

        if not school_tests:
            json_abort(400,"SchoolTests not found")
        else:
            return school_tests

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_all():
    try:
        school_tests = SchoolTests.query.all()

        if not school_tests:
            json_abort(400,"SchoolTests not found")
        else:
            return school_tests

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        school_tests = SchoolTests.query.filter_by(SchoolTestsID=id).first()

        if not school_tests:
            json_abort(400,"SchoolTests not found")
        else:

            title = data.get('Title')
            if not title:
                json_abort(400,"title is required")

            student_id = data.get('StudentID')
            if not student_id:
                json_abort(400,"StudentID is required")

            test_grade = data.get('TestGrade')
            if not test_grade:
                json_abort(400,"test_grade is required")

            concept = data.get('Concept')
            if not concept:
                json_abort(400,"concept is required")

 
            school_tests.Title = title
            school_tests.StudentID = student_id
            school_tests.TestGrade = test_grade
            school_tests.Concept = concept

            db.session.commit()
        
            return school_tests

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        school_tests = SchoolTests.query.filter_by(SchoolTestsID=id).first()

        if not school_tests:
            json_abort(400,"SchoolTests not found")
        else:
            db.session.delete(school_tests)
            db.session.commit()
        
            return school_tests

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)