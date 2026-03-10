from sqlalchemy import *
from connectionBD.config import *


def get_engine():
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        )
        return engine

    except Exception as e:
        print("Erreur connexion base :", e)
        return None