import pandas as pd

# List of CSV files and their primary key columns
csv_files = {
    'region.csv': ['Region_Name'],
    'etat.csv': ['State_Name'],
    'localisation.csv': ['Postal_Code'],
    'date_temps.csv': ['Order_Date'], 
    'client.csv': ['Customer_ID'],
    'categorie.csv': ['Category_Name'],
    'sous_categorie.csv': ['Sub_Category_Name'],
    'produit.csv': ['Product_ID'],
    'commande.csv': ['Order_ID'],
    'ventes_split.csv': ['Row_ID']
}

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