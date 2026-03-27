import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

USERNAME = os.getenv("DB_USER", "postgres")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "5432")
DATABASE = os.getenv("DB_NAME", "superstore_db")

if not PASSWORD:
    print("Warning: DB_PASSWORD is not set in the .env file.")
