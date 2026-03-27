import pandas as pd

def verifier_primary_keys():

    print("\n-------> verification des cles primaire")
    
    # --> List des fichier 
    csv_files = {
        'PostgreSQL/fichier_split/region.csv': ['region_name'],
        'PostgreSQL/fichier_split/etat.csv': ['state_name'],
        'PostgreSQL/fichier_split/localisation.csv': ['postal_code'],
        'PostgreSQL/fichier_split/date_temps.csv': ['order_date'], 
        'PostgreSQL/fichier_split/client.csv': ['customer_id'],
        'PostgreSQL/fichier_split/categorie.csv': ['category_name'],
        'PostgreSQL/fichier_split/sous_categorie.csv': ['sub_category_name'],
        'PostgreSQL/fichier_split/produit.csv': ['product_id'],
        'PostgreSQL/fichier_split/commande.csv': ['order_id'],
        'PostgreSQL/fichier_split/ventes_split.csv': ['row_id']
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
