import pandas as pd
import matplotlib.pyplot as plt


def graphes(Ventes_Catégorie , Ventes_region , profit_segment , top_product , G_moins):

    try :

        plt.figure()
        Ventes_Catégorie.plot(kind="bar")
        plt.bar(Ventes_Catégorie["Category"] , Ventes_Catégorie["Sales"])
        plt.title("Ventes par catégorie")
        plt.ylabel("Sales")
        plt.xlabel("Category")
        plt.savefig("fichier_livrable/Ventes_Catégorie")

        plt.figure()
        plt.bar(Ventes_region["Region"] , Ventes_region["Sales"])
        plt.title("Ventes par région")
        plt.ylabel("Sales")
        plt.xlabel("Region")
        plt.savefig("fichier_livrable/Ventes_region")

        plt.figure()
        plt.bar(profit_segment["Segment"] , profit_segment["Sales"])
        plt.title("Profit estimé par segment")
        plt.ylabel("Sales / Profit estimé")
        plt.xlabel("Segment")
        plt.savefig("fichier_livrable/Profit_segment")

        plt.figure()
        plt.barh(top_product["Product ID"] , top_product["Sales"])
        plt.title("Top 10 produits")
        plt.xlabel("Sales")
        plt.ylabel("Product ID")
        plt.xticks(rotation=30)
        plt.savefig("fichier_livrable/Top_produits")

        plt.figure()
        plt.plot(G_moins["mois"] , G_moins["Sales"] , marker="o")
        plt.title("Croissance mensuelle des ventes")
        plt.ylabel("Sales")
        plt.xlabel("Mois")
        plt.savefig("fichier_livrable/Croissance_mensuelle")


        
    except Exception as e :
        print("Erreur : " , e)
