import os
from os import environ as env
from dotenv import load_dotenv

# loadenv variable
load_dotenv()

# Statement for enabling the development environment
DEBUG = os.environ.get("DEBUG", True)

DB_TYPE = env.get('DB_TYPE', 'sqlite')
DB_NAME = env.get('DB_NAME', 'tests')
DB_URI = env.get('DB_URI', None)
# db path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

# Define the database - we are working with
# TEST_DB_NAME for sqllite, DB_URI for postgres
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'\
  if DB_TYPE == 'sqlite' else DB_URI

# print queries if debug
SQLALCHEMY_ECHO = True if DEBUG else False
# over head
SQLALCHEMY_TRACK_MODIFICATIONS = False

DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies, not secure.. testing only
SECRET_KEY = os.urandom(32)