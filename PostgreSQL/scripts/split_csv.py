import pandas as pd

def split_csv(path_csv):

    try:

        # --> read and clean fichier csv pour diviser
        df = pd.read_csv(path_csv, encoding='utf-8')
        df.columns = [col.strip().lower() for col in df.columns]

        # --> REGION
        df_region = df[['region']].drop_duplicates().reset_index(drop=True)
        df_region['region_id'] = df_region.index + 1
        df_region = df_region.rename(columns={'region': 'region_name'})
        df_region.to_csv('PostgreSQL/fichier_split/region.csv', index=False)

        # --> ETAT
        df_etat = df[['state', 'country', 'region']].drop_duplicates(subset=['state'])
        df_etat = df_etat.merge(df_region, left_on='region', right_on='region_name', how='left')
        df_etat = df_etat[['state', 'country', 'region_id']].rename(
            columns={'state': 'state_name'}
        )
        df_etat = df_etat.reset_index(drop=True)
        df_etat['state_id'] = df_etat.index + 1
        df_etat.to_csv('PostgreSQL/fichier_split/etat.csv', index=False)

        # --> LOCALISATION
        df_localisation = df[['postal code', 'city', 'state']].drop_duplicates(subset=['postal code'])
        df_localisation = df_localisation.merge(
            df_etat[['state_name', 'state_id']],
            left_on='state', right_on='state_name', how='left'
        )
        df_localisation = df_localisation[['postal code', 'city', 'state_id']].rename(
            columns={'postal code': 'postal_code'}
        )
        df_localisation.to_csv('PostgreSQL/fichier_split/localisation.csv', index=False)

        # --> DATE_TEMPS
        df_date_temps = df[['order date', 'annees', 'mois', 'trimestre']] \
            .drop_duplicates(subset=['order date']) \
            .rename(columns={'order date': 'order_date', 'annees': 'annee'}) \
            .reset_index(drop=True)
        df_date_temps['date_id'] = df_date_temps.index + 1
        df_date_temps.to_csv('PostgreSQL/fichier_split/date_temps.csv', index=False)

        # --> CLIENT
        df_client = df[['customer id', 'customer name', 'segment']] \
            .drop_duplicates(subset=['customer id']) \
            .rename(columns={
                'customer id': 'customer_id',
                'customer name': 'customer_name'
            })
        df_client.to_csv('PostgreSQL/fichier_split/client.csv', index=False)

        # --> CATEGORIE
        df_categorie = df[['category']].drop_duplicates().reset_index(drop=True)
        df_categorie['category_id'] = df_categorie.index + 1
        df_categorie = df_categorie.rename(columns={'category': 'category_name'})
        df_categorie.to_csv('PostgreSQL/fichier_split/categorie.csv', index=False)

        # --> SOUS_CATEGORIE
        df_sous_categorie = df[['sub-category', 'category']] \
            .drop_duplicates(subset=['sub-category'])
        df_sous_categorie = df_sous_categorie.merge(
            df_categorie,
            left_on='category',
            right_on='category_name',
            how='left'
        )
        df_sous_categorie = df_sous_categorie[['sub-category', 'category_id']] \
            .rename(columns={'sub-category': 'sub_category_name'}) \
            .reset_index(drop=True)
        df_sous_categorie['sub_category_id'] = df_sous_categorie.index + 1
        df_sous_categorie.to_csv('PostgreSQL/fichier_split/sous_categorie.csv', index=False)

        # --> PRODUIT
        df_produit = df[['product id', 'product name', 'sub-category']] \
            .drop_duplicates(subset=['product id'])
        df_produit = df_produit.merge(
            df_sous_categorie[['sub_category_name', 'sub_category_id']],
            left_on='sub-category',
            right_on='sub_category_name',
            how='left'
        )
        df_produit = df_produit[['product id', 'product name', 'sub_category_id']] \
            .rename(columns={
                'product id': 'product_id',
                'product name': 'product_name'
            })
        df_produit.to_csv('PostgreSQL/fichier_split/produit.csv', index=False)

        # --> COMMANDE
        df_commande = df[['order id', 'ship date', 'ship mode',
                          'customer id', 'postal code', 'order date',
                          'délais livraison']].drop_duplicates(subset=['order id'])
        df_commande = df_commande.merge(
            df_date_temps[['order_date', 'date_id']],
            left_on='order date',
            right_on='order_date',
            how='left'
        )
        df_commande = df_commande.rename(columns={
            'order id': 'order_id',
            'ship date': 'ship_date',
            'ship mode': 'ship_mode',
            'customer id': 'customer_id',
            'postal code': 'postal_code',
            'délais livraison': 'delais_livraison'
        })[['order_id', 'ship_date', 'ship_mode',
            'customer_id', 'postal_code',
            'date_id', 'delais_livraison']]
        df_commande['delais_livraison'] = df_commande['delais_livraison'] \
            .astype(str).str.extract(r'(\d+)').astype(int)
        df_commande.to_csv('PostgreSQL/fichier_split/commande.csv', index=False)

        # --> VENTES
        df_ventes = df[['row id', 'sales', 'quantity',
                        'marge_relative', 'taux_profit_estime',
                        'ratio_qte_sales', 'order id', 'product id']] \
            .drop_duplicates(subset=['row id']) \
            .rename(columns={
                'row id': 'row_id',
                'order id': 'order_id',
                'product id': 'product_id'
            })
        df_ventes.to_csv('PostgreSQL/fichier_split/ventes_split.csv', index=False)



        print("------>\n le fichier et deviser \n")

    except FileNotFoundError as e:
        print("Erreur fichier :", e)

    except Exception as e:
        print("Erreur :", e)