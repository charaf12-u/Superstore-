from sqlalchemy import text

def run_analytics(engine):
    try:
        with engine.connect() as conn:

            # --> les ventes par categorie
            print("\n ------> les ventes par categorie")
            result = conn.execute(text("""
                SELECT c.category_name, SUM(v.sales) AS total_sales
                FROM ventes v
                JOIN produit p ON v.product_id = p.product_id
                JOIN sous_categorie sc ON p.sub_category_id = sc.sub_category_id
                JOIN categorie c ON sc.category_id = c.category_id
                GROUP BY c.category_name
                ORDER BY total_sales DESC
                LIMIT 5
            """))
            for row in result:
                print(row)


            # --> les profit par region
            print("\n ------> les ventes par categorie")
            result = conn.execute(text("""
                SELECT r.region_name, SUM(v.taux_profit_estime) AS total_profit
                FROM ventes v
                JOIN commande co ON v.order_id = co.order_id
                JOIN localisation l ON co.postal_code = l.postal_code
                JOIN etat e ON l.state_id = e.state_id
                JOIN region r ON e.region_id = r.region_id
                GROUP BY r.region_name
                ORDER BY total_profit DESC
                LIMIT 5
            """))
            for row in result:
                print(row)


            # --> les top clients
            print("\n ------> les top clients")
            result = conn.execute(text("""
                SELECT cl.customer_name, SUM(v.sales) AS total_spent
                FROM ventes v
                JOIN commande co ON v.order_id = co.order_id
                JOIN client cl ON co.customer_id = cl.customer_id
                GROUP BY cl.customer_name
                ORDER BY total_spent DESC
                LIMIT 10
            """))
            for row in result:
                print(row)


            # --> les nombre commandes par mois
            print("\n ------> les nombre commandes par mois")
            result = conn.execute(text("""
                SELECT dt.annee, dt.mois, COUNT(co.order_id) AS total_commandes
                FROM commande co
                JOIN date_temps dt ON co.date_id = dt.date_id
                GROUP BY dt.annee, dt.mois
                ORDER BY dt.annee, dt.mois
                LIMIT 5
            """))
            for row in result:
                print(row)


    except Exception as e:
        print("Analytics error:", e)