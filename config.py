import os

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://postgres:password@localhost/jogoteca'

UPLOAD_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/uploads'