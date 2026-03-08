from sqlalchemy import create_engine
from scripts.config import USERNAME, PASSWORD, HOST, PORT, DATABASE
from scripts.create_tables import metadata
from scripts.insert_data import insert_data

engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

metadata.create_all(engine)

# insert des donner
tables_csv = [
    ('region',         'region.csv'),
    ('etat',           'etat.csv'),
    ('localisation',   'localisation.csv'),
    ('date_temps',     'date_temps.csv'),
    ('client',         'client.csv'),
    ('categorie',      'categorie.csv'),
    ('sous_categorie', 'sous_categorie.csv'),
    ('produit',        'produit.csv'),
    ('commande',       'commande.csv'),
    ('ventes',         'ventes_split.csv')
]

for table_name, csv_file in tables_csv:
    insert_data(engine, table_name, csv_file)