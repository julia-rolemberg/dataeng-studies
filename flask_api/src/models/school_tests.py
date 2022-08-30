from . import db

class SchoolTests(db.Model):
    __tablename__ = 'SchoolTests'

    SchoolTestsID = db.Column(db.Integer, primary_key=True) 
    Title = db.Column(db.Text())
    Created = db.Column(db.DateTime, default=db.func.now()) 
    StudentID = db.Column(
        db.Integer, db.ForeignKey('Student.StudentID', ondelete='CASCADE'))
    Student = db.relationship('Student')
    TestGrade = db.Column(db.Text())
    Concept = db.Column(db.Text())

    def __str__(self):
        return self.Title

    def get_school_tests_id(self):
        return self.SchoolTestsID