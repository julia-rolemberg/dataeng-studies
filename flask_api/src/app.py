import os
from flask import Flask, Blueprint 
#import configuracao
from src.config.restplus import api,init_config
from src.config.settings import config_by_name 
#import databese e models
from src.models import db
from src.models.course import Course
from src.models.student import Student
from src.models.school_tests import SchoolTests
#import blueprint controllers
from src.api.student_controller import ns as student_namespace
from src.api.course_controller import ns as course_namespace
from src.api.school_tests_controller import ns as school_tests_namespace


   
    
def create_app(config_name):
    #inicia flask
    app = Flask(__name__)
    #inicia configuracao variaveis de ambiente
    app.config.from_object(config_by_name[config_name])

    setup_app(app)

    return app


def setup_app(app):
    # cria as tabelas se elas nao existirem ainda
    @app.before_first_request
    def create_tables():
        db.create_all()
 
    #inicia base de dados
    db.init_app(app) 

    #congirura blueprint para as rotas com namespace
    blueprint = Blueprint('api', __name__, url_prefix='/api')

    #adiciona blueprint no app 
    api.init_app(blueprint)
    #chama a funcao que vai congigurar as API
    init_config(app)
    #adiciona namespaces to blueprint
    api.add_namespace(course_namespace)
    api.add_namespace(student_namespace) 
    api.add_namespace(school_tests_namespace) 

    #registra blueprint
    app.register_blueprint(blueprint, url_prefix='')
    
    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')