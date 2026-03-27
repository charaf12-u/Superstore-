from sqlalchemy import create_url, create_engine
from src.database.config import USERNAME, PASSWORD, HOST, PORT, DATABASE

def get_engine():
    url = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    return create_engine(url)
