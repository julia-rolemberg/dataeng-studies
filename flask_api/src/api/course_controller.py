from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.course_serializer import course_request, course_result, course_students_result
from src.services.course_service import create, change, delete, get, get_course_students, get_all
 

ns = api.namespace('api/course', description='Operations related to course')


@ns.route('/<int:id>/students')
class CourseStudentsCollection(Resource):
    @api.marshal_with(course_students_result)
    def get(self,id):
    
        course = get_course_students(id)
        return course


@ns.route('')
class CourseCollection(Resource):
    @api.expect(course_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(course_result)#define resultado da metodo 
    def post(self):
        course = create(request.json)
        return course 

    @api.marshal_with(course_result)#define resultado da metodo 
    def get(self):
        course_list = get_all()
        return course_list

 

@ns.route('/<int:id>')
class CourseIDCollection(Resource): 
    @api.marshal_with(course_result)
    def get(self, id):

        course = get(id)
        return course 


    @api.expect(course_request)
    @api.marshal_with(course_result)
    def put(self, id):

        course = change(id,request.json)
        return course 
 
    @api.marshal_with(course_result)
    def delete(self, id):

        course = delete(id)
        return course 