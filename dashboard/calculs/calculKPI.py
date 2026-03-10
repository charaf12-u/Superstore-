

def calculKPI(df) :
    try :
        

        # --> Calculer des métriques clés
        totalSales = df["sales"].sum()
        totalProfit = df["marge_relative"].sum()
        averageProfit = df["marge_relative"].mean()
        totalQuantite = df["quantity"].sum()
        NBcommande = len(df)

        print("total sales = " , totalSales)
        print("total profit = " , totalProfit)
        print("average profit = " , averageProfit)
        print("total quantites = " , totalQuantite)
        print("nomber de command = " , NBcommande)


        # --> Calculer statistiques de base
        MoyenneV = df["sales"].mean()
        médianeV = df["sales"].median()
        minimumV = df["sales"].min()
        maximumV = df["sales"].max()
        écart_typeV = df["sales"].std()

        print("\nmoyeen sales = " , MoyenneV)
        print("médiane sales = " , médianeV)
        print("min sales = " , minimumV)
        print("max sales = " , maximumV)
        print("écart_type sales = " , écart_typeV)
    

    except Exception as e :
        print("erreur : ",e )