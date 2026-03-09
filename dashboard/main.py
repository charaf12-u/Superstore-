from connectionBD.db_connection import get_engine

engine = get_engine()

if engine:
    print("La base est prête pour les requêtes")