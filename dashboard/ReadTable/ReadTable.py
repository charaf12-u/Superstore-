import pandas as pd 



def readTable(engine) :
    try : 

        listTable = [
            "ventes","produit","sous_categorie","categorie","commande","client",
            "date_temps","localisation","etat","region" 
        ]

        for col in listTable :
            df = pd.read_sql_table(col , engine)
            print("\n ------> table : ", col)
            print(df.head())        


    except Exception as e: 
        print("erreur : " , e )