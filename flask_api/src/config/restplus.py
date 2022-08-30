 
from flask import jsonify
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from src.config import settings
 

    
#Configura nome da API e documentaçao do swagger 
api = Api(version='1.0', title=' Post Service API',
          description='Api de gestão de posts ' )
    
#formata retorno de erro
def json_abort(status_code, message):
    data = {
        'error': {
            'code': status_code,
            'message': message
        }
    }
    response = jsonify(data)
    response.status_code = status_code
    api.abort(response)

#fix para nao aparecer o parametro x-field no swagger
def init_config(app):
    app.config['RESTPLUS_MASK_SWAGGER'] = False

 