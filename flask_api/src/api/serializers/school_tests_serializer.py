from flask_restplus import fields
from src.config.restplus import api


school_tests_request = api.model('School Tests Request', {
    'Title': fields.String(required=True, description='name'),
    'StudentID': fields.Integer(required=True, description='student'),
    'TestGrade': fields.String(required=True, description='testgrade'),    
    'Concept' : fields.String(required=True, description='concept')

})

school_tests_result = api.model('School Tests Result', {
    'SchoolTestsID': fields.Integer(required=True, description='Post Id'),
    'Title': fields.String(required=True, description='name'),
    'StudentID': fields.Integer(required=True, description='student'),
    'TestGrade': fields.String(required=True, description='testgrade'),    
    'Concept' : fields.String(required=True, description='concept'),
    'Created': fields.DateTime(required=True, description='school tests created date')

})
