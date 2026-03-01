import pandas as pd
from .fun import *
from .graphes import *
from .rapport import *


def read_clean(fichier_rntrer="fichier_data/store.csv" , fichier_sortie="fichier_livrable/superstore_clean.csv"):

    try :

        # read and clean data 
        df = pd.read_csv(fichier_rntrer)
        pd.set_option('display.max_columns' , None)
        df_A = df.drop_duplicates().copy()
        # modifier les types des columns
        dfListInt = ["Row ID", "Postal Code"]
        dfListDate = ["Order Date" ,"Ship Date" ]
        dfListCategory = ["Segment" , "Region" , "Category" , "Sub-Category"]
        dfString = ["Ship Mode" , "Customer Name" , "Country" ,
                     "City" , "State"  , "Product Name"]
       
        df_A.rename(columns={"Sales;": "Sales"}, inplace=True)
        df_A["Sales"] = (
        df_A["Sales"].astype(str).str.replace(";", "", regex=False))

        df_A = IntType(df_A, dfListInt)
        df_A = dateType(df_A , dfListDate)
        df_A = CategoryType(df_A , dfListCategory)
        df_A["Sales"] = pd.to_numeric(df_A["Sales"], errors="coerce")
        df_A = StringType(df_A , dfString)


        # remove NaN
        df_A = df_A.dropna()

        # extraction de anneés , mois , trimestre
        df_A["Annees"] = df_A["Order Date"].dt.year
        df_A["mois"] = df_A["Order Date"].dt.month
        df_A["trimestre"] = df_A["Order Date"].dt.quarter

        # calcul marge 
        df_A["Marge_relative"] = df_A["Sales"] / df_A.groupby("Product ID")["Sales"].transform("sum")
        df_A["Taux_profit_estime"] = df_A["Sales"] / df_A["Sales"].sum()
        df_A["Quantity"] = 1
        df_A["Ratio_Qte_Sales"] = df_A["Quantity"] / df_A["Sales"]

        # calcule délais livraison
        df_A["délais livraison"] = df_A["Ship Date"] - df_A["Order Date"]

        # specifier les data Transformation dans un neau data frame
        df_Transformation = df_A[["Marge_relative" , "Taux_profit_estime" , "Ratio_Qte_Sales" ,
                                 "délais livraison"]].copy()
        df_Transformation.reset_index(drop=True, inplace=True)

        # les valeurs aberrantes
        q1 = df_A["Sales"].quantile(0.25)
        q3 = df_A["Sales"].quantile(0.75)

        IQR = q3 - q1
        lower_range = q1 - 1.5 * IQR
        upper_range = q3 + 1.5 * IQR
        # data fram anormalis 
        df_anormalis = df_A[(df_A["Sales"] < lower_range) | (df_A["Sales"] > upper_range)
                        ][["Row ID" , "Order ID" , "Customer ID" , "Product ID" , "Sales"]]
        # data normal
        df_A = df_A[(df_A["Sales"] > lower_range) & (df_A["Sales"] < upper_range)]
        
        # Ventes par catégorie
        Ventes_Catégorie = df_A.groupby("Category")["Sales"].sum().reset_index()
        print(Ventes_Catégorie)
        # Ventes par region
        Ventes_region = df_A.groupby("Region")["Sales"].sum().reset_index()
        # Profit par segment
        profit_segment = df_A.groupby("Segment")["Sales"].sum().reset_index()
        # top product 
        top_product = df_A.groupby("Product ID")["Sales"].sum()
        top_product = top_product.sort_values(ascending=False).head(10).reset_index()
        # Croissance mensuelle
        G_moins = df_A.groupby("mois")["Sales"].sum().reset_index()
        
        # export data to fichier
        df_A.to_csv(fichier_sortie)

        graphes(Ventes_Catégorie , Ventes_region , profit_segment , top_product , G_moins)

        create_report_word(df , df_A , df_Transformation , df_anormalis ,Ventes_Catégorie , 
                Ventes_region , profit_segment , top_product , G_moins
                , filename="fichier_livrable/rapport.docx")

    
    
    except FileExistsError as e:
        print("Erreur : " , e)

    except Exception as e :
        print("Erreur : " , e)
