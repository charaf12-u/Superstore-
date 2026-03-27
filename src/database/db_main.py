from src.database.db_connection import get_engine
from src.database.create_tables import metadata
from src.database.split_csv import split_csv
from src.database.check_uniqueness import verifier_primary_keys
from src.database.insert_data import insert_data
import os

def run_db_pipeline(csv_path="data/processed/superstore_clean.csv"):
    print("--- Starting Database Pipeline ---")
    
    # 1. Get Engine
    engine = get_engine()
    
    # 2. Create Tables
    print("Creating tables...")
    metadata.create_all(engine)
    
    # 3. Split CSV
    print("Splitting CSV data...")
    split_csv(csv_path)
    
    # 4. Check Uniqueness
    print("Verifying data integrity...")
    verifier_primary_keys()
    
    # 5. Insert Data
    print("Inserting data into PostgreSQL...")
    tables_to_insert = [
        ('region', 'data/processed/sql_splits/region.csv'),
        ('etat', 'data/processed/sql_splits/etat.csv'),
        ('localisation', 'data/processed/sql_splits/localisation.csv'),
        ('date_temps', 'data/processed/sql_splits/date_temps.csv'),
        ('client', 'data/processed/sql_splits/client.csv'),
        ('categorie', 'data/processed/sql_splits/categorie.csv'),
        ('sous_categorie', 'data/processed/sql_splits/sous_categorie.csv'),
        ('produit', 'data/processed/sql_splits/produit.csv'),
        ('commande', 'data/processed/sql_splits/commande.csv'),
        ('ventes', 'data/processed/sql_splits/ventes_split.csv'),
    ]
    
    for table_name, file_path in tables_to_insert:
        insert_data(engine, table_name, file_path)
        
    print("--- Database Pipeline Completed Successfully ---")

if __name__ == "__main__":
    # Ensure raw data is processed first or use the processed one
    processed_data = "data/processed/superstore_clean.csv"
    if os.path.exists(processed_data):
        run_db_pipeline(processed_data)
    else:
        print(f"Error: Processed data not found at {processed_data}. Please run main.py first.")
