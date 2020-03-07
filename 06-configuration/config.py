"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = True
    DEBUG = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SESSION_COOKIE_NAME = 'my_cookie'

    # From .env
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')

# we can have more config variations
class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

# some other configuraiton
# FLASK_ENV
# DEBUG
# TESTING
# SECRET_KEY
# SERVER_NAME

# ASSETS_DEBUG
# COMPRESSOR_DEBUG
# FLASK_ASSETS_USE_S3
# FLASK_ASSETS_USE_CDN

# SQLALCHEMY_DATABASE_URI
# SQLALCHEMY_ECHO
# SQLALCHEMY_ENGINE_OPTIONS

# SESSION_TYPE
# SESSION_PERMANENT
# SESSION_KEY_PREFIX
# SESSION_REDIS
# SESSION_MEMCASHED
# SESSION_MONGODB
# SESSION_SQLALCHEMY
