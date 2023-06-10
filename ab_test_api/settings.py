import dotenv
import os
from urllib.parse import urlparse

dotenv.load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

MIN_CONN = int(os.getenv('MIN_CONN', 1))
MAX_CONN = int(os.getenv('MAX_CONN', 20))

DATABASE_URL = urlparse(os.getenv('DATABASE_URL'))

if DATABASE_URL:
    DB_HOST = DATABASE_URL.hostname
    DB_PORT = DATABASE_URL.port
    DB_NAME = DATABASE_URL.path[1:]
    DB_USER = DATABASE_URL.username
    DB_PASS = DATABASE_URL.password
