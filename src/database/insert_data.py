import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert as pg_insert
from scripts.create_tables import metadata

def insert_data(engine, table_name, csv_file):
    
    try:
        # --> get table en dectionnair metadata
        table = metadata.tables.get(table_name)

        # --> pour table None
        if table is None:
            print(f"[ERREUR] Table '{table_name}' non trouvée !")
            return
        
        # --> tahwil rows in dictionnaire
        df = pd.read_csv(csv_file)
        df.columns = [col.lower() for col in df.columns]
        records = df.to_dict(orient='records')

        # --> enregistrer les rows
        with engine.begin() as conn:
            stmt = pg_insert(table).values(records).on_conflict_do_nothing()
            conn.execute(stmt)

        print(table_name ,' inserte ')

    except FileNotFoundError as e:
        print("erreur : ", e)
    except SQLAlchemyError as e:
        print("erreur : ", e)
    except Exception as e:
        print("erreur : ", e)
