from . import db

#configura modelo de dados do POST
class Student(db.Model):
    __tablename__ = 'Student'

    StudentID = db.Column(db.Integer, primary_key=True) 
    Name = db.Column(db.Text())
    Created = db.Column(db.DateTime, default=db.func.now()) 
    CourseID = db.Column(
        db.Integer, db.ForeignKey('Course.CourseID', ondelete='CASCADE'))
    Course = db.relationship('Course')
    Age = db.Column(db.Integer)
    CPF = db.Column(db.String)

    def __str__(self):
        return self.Name

    def get_student_id(self):
        return self.StudentID