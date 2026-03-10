import pandas as pd
from connectionBD.db_connection import *
from ReadTable.ReadTable import *
from extarctionDonnes.extractionDonnes import *

engine = get_engine()


if engine:
    print("La base est prête pour les requêtes")

readTable(engine)
run_analytics(engine)

