import dotenv
import os
from urllib.parse import urlparse

dotenv.load_dotenv()
env = os.environ.get

DATABASE_URL = urlparse(env('DATABASE_URL'))

if DATABASE_URL:
    DB_HOST = DATABASE_URL.hostname
    DB_PORT = DATABASE_URL.port
    DB_NAME = DATABASE_URL.path[1:]
    DB_USER = DATABASE_URL.username
    DB_PASS = DATABASE_URL.password
else:
    DB_HOST = env('DB_HOST')
    DB_PORT = env('DB_PORT')
    DB_NAME = env('DB_NAME')
    DB_USER = env('DB_USER')
    DB_PASS = env('DB_PASS')

MAX_CONN = int(env('MAX_CONN'))
MIN_CONN = int(env('MIN_CONN'))
