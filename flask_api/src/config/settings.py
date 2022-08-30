 
import os 


### Congiruracao das variaveis de ambiente e database
###
###


basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
 
    # General Config 
    DEBUG = False
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
     
   
class DevelopmentConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:2cHeraKa81N6by9B@localhost:33306/EngagePost')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config): 
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'productionUser.db')


config_by_name = dict(
    DEV=DevelopmentConfig,
    TEST=TestingConfig,
    PROD=ProductionConfig
)

key = Config.SECRET_KEY
 