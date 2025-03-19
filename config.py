import os

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = \
    'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')

# SQLALCHEMY_DATABASE_URI = \
#     'postgresql+psycopg2://postgres:password@localhost/jogoteca'

UPLOAD_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/uploads'