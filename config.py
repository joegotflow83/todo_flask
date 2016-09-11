from secret import db_name, db_username, db_password, secret_key

import os


basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = db_name
USERNAME = db_username
PASSWORD = db_password
WTF_CSRF_ENABLED = True
SECRET_KEY = secret_key

# Database path
DATABASE_PATH = os.path.join(basedir, DATABASE)
