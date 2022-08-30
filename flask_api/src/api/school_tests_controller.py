from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.school_tests_serializer import school_tests_result, school_tests_request
from src.services.school_tests_service import create, change, delete, get, get_all
 

ns = api.namespace('api/schooltests', description='Operations related to school tests')


@ns.route('') # define rota
class SchoolTestsCollection(Resource):
    @api.expect(school_tests_request) #define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(school_tests_result) #define resultado da metodo 
    def post(self):
 
        school_tests = create(request.json)
        return school_tests 
    
    @api.marshal_with(school_tests_result) #define resultado da metodo 
    def get(self):

        school_tests = get_all()
        
        return school_tests


 

@ns.route('/<int:id>')
class SchoolTestsIDCollection(Resource): 
    @api.marshal_with(school_tests_result)
    def get(self, id):
        school_tests = get(id)
        return school_tests 


    @api.expect(school_tests_request)
    @api.marshal_with(school_tests_result)
    def put(self, id):

        school_tests = change(id,request.json)
        return school_tests 
 
    @api.marshal_with(school_tests_result)
    def delete(self, id):

        school_tests = delete(id)
        return school_tests 