from src.models import db
from src.models.course import Course
from src.models.student import Student
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 


def create(data):
    try:
        Name = data.get('Name')
        if not Name:
            json_abort(400,"Name is required")

        StudyArea = data.get('StudyArea')
        if not StudyArea:
            json_abort(400,"StudyArea is required")

        course = Course(Name=Name,StudyArea=StudyArea)
        db.session.add(course)
        db.session.commit()

        return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        course = Course.query.filter_by(CourseID=id).first()

        if not course:
            json_abort(400,"course not found")
        else:
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_all():
    try:
        
        course = Course.query.all()

        if not course:
            json_abort(400, "Course not found")
        else:
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error) 

def get_course_students(id):
    try:
        course = Course.query.filter_by(CourseID=id).first()
        course.listStudents = Student.query.filter_by(CourseID=id).all()
        
        if not course:
            json_abort(400,"course not found")
        else:
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def change(id, data):
    try:
        
        course = Course.query.filter_by(CourseID=id).first()

        if not course:
            json_abort(400,"Course not found")
        else:

            Name = data.get('Name')
            if not Name:
                json_abort(400,"Name is required")

            StudyArea = data.get('StudyArea')
            if not StudyArea:
                json_abort(400,"StudyArea is required")

            course.Name = Name
            course.StudyArea = StudyArea
           
            db.session.commit()
        
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        course = Course.query.filter_by(CourseID=id).first()

        if not course:
            json_abort(400,"course not found")
        else:
            db.session.delete(course)
            db.session.commit()
        
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)