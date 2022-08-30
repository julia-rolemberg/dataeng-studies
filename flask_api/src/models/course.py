from . import db 

class Course(db.Model):
    __tablename__ = 'Course'

    CourseID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    StudyArea = db.Column(db.String(255)) 

    def __str__(self):
        return self.Name

    def get_course_id(self):
        return self.CourseID
