from sqlalchemy import text

def run_tests(engine):

    try:
        with engine.connect() as conn:
            
            # --> test count(*)
            print("\n ------> TEST COUNT")
            tables = [
                "region","etat","localisation","date_temps",
                "client","categorie","sous_categorie",
                "produit","commande","ventes"
            ]
            for t in tables:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {t}"))
                count = result.scalar()
                print(f"{t} : {count} rows")


            # --> test les Jointure
            print("\n ------> TEST JOIN")
            #  region -> etat
            result = conn.execute(text("""
                SELECT e.state_name, r.region_name
                FROM etat e
                JOIN region r
                ON e.region_id = r.region_id
                LIMIT 5
            """))
            for row in result:
                print(row)

            # localisation -> etat
            result = conn.execute(text("""
                SELECT l.city, e.state_name
                FROM localisation l
                JOIN etat e
                ON l.state_id = e.state_id
                LIMIT 5
            """))
            for row in result:
                print(row)

            # ventes -> commande
            result = conn.execute(text("""
                SELECT v.sales, c.order_id
                FROM ventes v
                JOIN commande c
                ON v.order_id = c.order_id
                LIMIT 5
            """))
            for row in result:
                print(row)


            # --> test les FK
            print("\n ------> TEST FK")
            try:
                conn.execute(text("""
                    INSERT INTO etat (state_name, country, region_id)
                    VALUES ('fake_state','usa',9999)
                """))
            except Exception:
                print("FK region -> etat works correctly")


            # --> test les CHECK
            print("\n ------> TEST CHECK")
            try:
                conn.execute(text("""
                    INSERT INTO ventes (sales, quantity, order_id, product_id)
                    VALUES (-10,1,'CA-2017-152156','FUR-BO-10001798')
                """))
            except Exception:
                print("CHECK constraint sales > 0 works\n")


    except Exception as e:
        print("Test error:", e)