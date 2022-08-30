from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.school_tests_serializer import school_tests_result


student_request = api.model('Student Request', {
    'Name': fields.String(required=True, description='name'),
    'CourseID': fields.Integer(required=True, description='course'),
    'Age': fields.Integer(required=True, description='age'),    
    'CPF' : fields.String(required=True, description='cpf')

})

student_result = api.model('Student Result', {
    'StudentID': fields.Integer(required=True, description='Student Id'),
    'Name': fields.String(required=True, description='name'),
    'CourseID': fields.Integer(required=True, description='course'),
    'Age': fields.Integer(required=True, description='age'),    
    'CPF' : fields.String(required=True, description='cpf'),
    'created': fields.DateTime(required=True, description='Student create date')

})

student_schooltests_result = api.model('Student School Tests Result', {
    'StudentID': fields.Integer(required=True, description='Student Id'),
    'Name': fields.String(required=True, description='name'),
    'CourseID': fields.Integer(required=True, description='course'),
    'Age': fields.Integer(required=True, description='age'),    
    'CPF' : fields.String(required=True, description='cpf'),
    'created': fields.DateTime(required=True, description='Student create date'),
    'listSchoolTests' : fields.List(fields.Nested(school_tests_result), description='list school tests')
})