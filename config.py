import os

DEBUG = True

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3307/flask_blog'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True