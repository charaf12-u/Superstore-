from sqlalchemy import (
    Table, Column, Integer, String, Numeric,
    Date, ForeignKey, MetaData, CheckConstraint
)

metadata = MetaData()

# --> table REGION
REGION = Table(
    'region', metadata,
    Column('region_id', Integer, primary_key=True, autoincrement=True),
    Column('region_name', String(30), nullable=False, unique=True)
)

# --> table ETAT
ETAT = Table(
    'etat', metadata,
    Column('state_id', Integer, primary_key=True, autoincrement=True),
    Column('state_name', String(100), nullable=False),
    Column('country', String(50), nullable=False),
    Column('region_id', Integer, ForeignKey('region.region_id',
                                            ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
)

# --> table LOCALISATION
LOCALISATION = Table(
    'localisation', metadata,
    Column('postal_code', String(20), primary_key=True),
    Column('city', String(100), nullable=False),
    Column('state_id', Integer, ForeignKey('etat.state_id',
                                           ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
)

# --> table DATE_TEMPS
DATE_TEMPS = Table(
    'date_temps', metadata,
    Column('date_id', Integer, primary_key=True, autoincrement=True),
    Column('order_date', Date, nullable=False, unique=True),
    Column('annee', Integer, nullable=False),
    Column('mois', Integer, nullable=False),
    Column('trimestre', Integer, nullable=False),
    CheckConstraint('mois BETWEEN 1 AND 12', name='ck_mois'),
    CheckConstraint('trimestre BETWEEN 1 AND 4', name='ck_trimestre')
)

# --> table CLIENT
CLIENT = Table(
    'client', metadata,
    Column('customer_id', String(20), primary_key=True),
    Column('customer_name', String(100), nullable=False),
    Column('segment', String(30), nullable=False),
    CheckConstraint(
        "segment IN ('consumer', 'corporate', 'home office')",
        name='ck_segment'
    )
)

# --> table COMMANDE
COMMANDE = Table(
    'commande', metadata,
    Column('order_id', String(20), primary_key=True),
    Column('ship_date', Date, nullable=False),
    Column('ship_mode', String(30), nullable=False),
    Column('delais_livraison', Integer, nullable=False),
    Column('customer_id', String(20), ForeignKey('client.customer_id',
                                                 ondelete='RESTRICT', onupdate='CASCADE'), nullable=False),
    Column('postal_code', String(20), ForeignKey('localisation.postal_code',
                                                 ondelete='RESTRICT', onupdate='CASCADE'), nullable=False),
    Column('date_id', Integer, ForeignKey('date_temps.date_id',
                                          ondelete='RESTRICT', onupdate='CASCADE'), nullable=False),
    CheckConstraint('delais_livraison >= 0', name='ck_delais'),
    CheckConstraint(
        "ship_mode IN ('first class','second class','standard class','same day')",
        name='ck_ship_mode'
    )
)

# --> table CATEGORIE
CATEGORIE = Table(
    'categorie', metadata,
    Column('category_id', Integer, primary_key=True, autoincrement=True),
    Column('category_name', String(50), nullable=False, unique=True)
)

# --> table SOUS_CATEGORIE
SOUS_CATEGORIE = Table(
    'sous_categorie', metadata,
    Column('sub_category_id', Integer, primary_key=True, autoincrement=True),
    Column('sub_category_name', String(50), nullable=False),
    Column('category_id', Integer, ForeignKey('categorie.category_id',
                                             ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
)

# --> table PRODUIT
PRODUIT = Table(
    'produit', metadata,
    Column('product_id', String(30), primary_key=True),
    Column('product_name', String(250), nullable=False),
    Column('sub_category_id', Integer, ForeignKey('sous_categorie.sub_category_id',
                                                 ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
)

# --> table VENTES
VENTES = Table(
    'ventes', metadata,
    Column('row_id', Integer, primary_key=True, autoincrement=True),
    Column('sales', Numeric(12, 2), nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('marge_relative', Numeric(10, 6), nullable=True),
    Column('taux_profit_estime', Numeric(12, 8), nullable=True),
    Column('ratio_qte_sales', Numeric(10, 6), nullable=True),
    Column('delais_livraison', Integer, nullable=True), 
    Column('order_id', String(20), ForeignKey('commande.order_id',
                                              ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
    Column('product_id', String(30), ForeignKey('produit.product_id',
                                                ondelete='RESTRICT', onupdate='CASCADE'), nullable=False),
    CheckConstraint('sales > 0', name='ck_sales'),
    CheckConstraint('quantity > 0', name='ck_quantity')
)