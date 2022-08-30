from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.student_serializer import student_result

course_request = api.model('Course Request', {
    'Name': fields.String(required=True, description='course name'),
    'StudyArea' : fields.String(required=True, description='course studyArea')

})

course_result = api.model('Course Result', {
    'CourseID': fields.Integer(required=True, description='Post Id'),
    'Name': fields.String(required=True, description='course name'),
    'StudyArea' : fields.String(required=True, description='course studyArea')

})


course_students_result = api.model('Course Students Result', {
    'CourseID': fields.Integer(required=True, description='Post Id'),
    'Name': fields.String(required=True, description='course name'),
    'StudyArea' : fields.String(required=True, description='course studyArea'),
    'listStudents' : fields.List(fields.Nested(student_result), description='list students')
})