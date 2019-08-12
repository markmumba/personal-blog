import os

class Config:
	# general configaration class

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SECRET_KEY = 'bobbyshmurda'

	# email configarations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG =True 

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mmark:123@localhost/blog_test'
    DEBUG =True 

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mark:123@localhost/hub'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 
    




