# Database configuration
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": "your_database_host",
    "user": "your_database_user",
    "password": os.getenv('DB_PASSWORD'),
    "database": "your_database_name",
}