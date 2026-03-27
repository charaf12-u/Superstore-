import pandas as pd

def verifier_primary_keys():

    print("\n-------> verification des cles primaire")
    
    # --> List des fichier 
    csv_files = {
        'data/processed/sql_splits/region.csv': ['region_name'],
        'data/processed/sql_splits/etat.csv': ['state_name'],
        'data/processed/sql_splits/localisation.csv': ['postal_code'],
        'data/processed/sql_splits/date_temps.csv': ['order_date'], 
        'data/processed/sql_splits/client.csv': ['customer_id'],
        'data/processed/sql_splits/categorie.csv': ['category_name'],
        'data/processed/sql_splits/sous_categorie.csv': ['sub_category_name'],
        'data/processed/sql_splits/produit.csv': ['product_id'],
        'data/processed/sql_splits/commande.csv': ['order_id'],
        'data/processed/sql_splits/ventes_split.csv': ['row_id']
    }

    # --> verifier la seul primary keys
    for file, pk_columns in csv_files.items():
        try:
            df = pd.read_csv(file)
            for col in pk_columns:
                duplicates = df[df.duplicated(subset=[col], keep=False)]
                if duplicates.empty:
                    print(f"[OK] Tous les {col} dans {file} sont uniques ")
                else:
                    print(f"[ERREUR] Doublons trouvés pour {col} dans {file} ")
                    print(duplicates[[col]])
        except FileNotFoundError:
            print(f"[ERREUR] Fichier {file} introuvable !")
