import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:annblue@localhost/pizza'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:annblue@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    #email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'annaadhiambo01gmail.com'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:annblue@localhost/pitch'

    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgcopg2://moringa:annblue@localhost/pitches'

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:annblue@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}