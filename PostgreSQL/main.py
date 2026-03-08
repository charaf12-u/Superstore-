from sqlalchemy import *
from scripts.config import USERNAME, PASSWORD, HOST, PORT, DATABASE
from scripts.create_tables import *
from scripts.insert_data import *
from tests.test_insertion import *
from scripts.split_csv import *
from scripts.check_uniqueness import *
from tests.test_analytics import *

engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# --> diviser le fichier data_csv
split_csv("fichier_livrable/superstore_clean.csv")

# --> verification de seul primary keys
verifier_primary_keys()

# --> creation des table
metadata.create_all(engine)


# --> insert des donner
print("\n-------> L'insertion des donner ")
tables_csv = [
    ('region',         'PostgreSQL/fichier_split/region.csv'),
    ('etat',           'PostgreSQL/fichier_split/etat.csv'),
    ('localisation',   'PostgreSQL/fichier_split/localisation.csv'),
    ('date_temps',     'PostgreSQL/fichier_split/date_temps.csv'),
    ('client',         'PostgreSQL/fichier_split/client.csv'),
    ('categorie',      'PostgreSQL/fichier_split/categorie.csv'),
    ('sous_categorie', 'PostgreSQL/fichier_split/sous_categorie.csv'),
    ('produit',        'PostgreSQL/fichier_split/produit.csv'),
    ('commande',       'PostgreSQL/fichier_split/commande.csv'),
    ('ventes',         'PostgreSQL/fichier_split/ventes_split.csv')
]
for table_name, csv_file in tables_csv:
    insert_data(engine, table_name, csv_file)

# --> test l'insertion
run_tests(engine)

# --> analys des vents
run_analytics(engine)