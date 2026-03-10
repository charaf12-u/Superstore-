import pandas as pd
from connectionBD.db_connection import *
from ReadTable.ReadTable import *
from extarctionDonnes.extractionDonnes import *
from extarctionDonnes.preparationDonnes import *
from calculs.calculKPI import *

engine = get_engine()


if engine:
    print("La base est prête pour les requêtes")

readTable(engine)
run_analytics(engine)

df = preparation(engine)
print(df)

print(df["order_date"].dtype)

# --> vérifier les nomber des columns null
print(df.isnull().sum())

calculKPI(df)