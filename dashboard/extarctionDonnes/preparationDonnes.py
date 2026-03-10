import pandas as pd
from connectionBD.db_connection import *

def preparation(engine):
    try :
        
        print("\n ------> preparation des donnes ")
        query = """
            SELECT v.sales, v.marge_relative, v.quantity,
                   r.region_name,
                   c.category_name,
                   d.order_date
            FROM ventes v
            JOIN commande co ON v.order_id = co.order_id
            JOIN date_temps d ON co.date_id = d.date_id
            JOIN produit p ON v.product_id = p.product_id
            JOIN sous_categorie sc ON p.sub_category_id = sc.sub_category_id
            JOIN categorie c ON sc.category_id = c.category_id
            JOIN client cl ON co.customer_id = cl.customer_id
            JOIN localisation l ON co.postal_code = l.postal_code
            JOIN etat e ON l.state_id = e.state_id
            JOIN region r ON e.region_id = r.region_id
        """

        df = pd.read_sql(query , engine )

        return df

    except Exception as e :
        print("erreur : ", e)