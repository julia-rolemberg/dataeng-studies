from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.student_serializer import student_request, student_result, student_schooltests_result
from src.services.student_service import create, change, delete, get, get_student_schoolTest, get_all
 

ns = api.namespace('api/student', description='Operations related to student')

@ns.route('/<int:id>/schooltest')
class StudentSchoolCollection(Resource):
    @api.marshal_with(student_schooltests_result)
    def get(self,id):
        
        student = get_student_schoolTest(id)
        return student


@ns.route('')#define rota
class StudentCollection(Resource):
    @api.expect(student_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(student_result)#define resultado da metodo 
    def post(self):
        student = create(request.json)
        return student 

    @api.marshal_with(student_result)#define resultado da metodo 
    def get(self):
        student_list = get_all()
        return student_list

 

@ns.route('/<int:id>')
class StudentIDCollection(Resource): 
    @api.marshal_with(student_result)
    def get(self, id):
      
        student = get(id)
        return student 


    @api.expect(student_request)
    @api.marshal_with(student_result)
    def put(self, id):
      
        student = change(id,request.json)
        return student 
 
    @api.marshal_with(student_result)
    def delete(self, id):
        
        student = delete(id)
        return student 