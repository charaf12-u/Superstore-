from sqlalchemy import *
from config import *


def get_engine():
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        )

        print("Connexion PostgreSQL réussie")
        return engine

    except Exception as e:
        print("Erreur connexion base :", e)
        return None