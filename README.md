# Superstore Sales: ETL, Analysis & PostgreSQL Integration

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/database-PostgreSQL-336791.svg)](https://www.postgresql.org/)

Ce projet fournit une solution automatisée pour le cycle de vie des données de ventes du dataset Superstore. Il transforme un fichier CSV plat en une base de données relationnelle normalisée (3NF) et génère des rapports d'analyse décisionnelle.

---

## Architecture du Projet

Le projet est structuré de manière modulaire pour faciliter la maintenance et l'évolution des composants.

```text
Superstore-Project
├── main.py                     # Orchestrateur du pipeline (Nettoyage -> Rapport)
├── src/                        # Code source du projet
│   ├── cleaning/               # Moteur d'ETL (read_clean_data.py, fun.py)
│   ├── visual/                 # Analytique Visuelle (graphes.py)
│   ├── reporting/              # Génération de rapports Word (rapport.py)
│   └── database/               # Couche de Persistance
│       ├── db_main.py          # Script d'orchestration de la base de données
│       ├── create_tables.py    # Définition du schéma SQL (SQLAlchemy)
│       ├── split_csv.py        # Logique de normalisation
│       ├── check_uniqueness.py # Validation d'intégrité
│       ├── db_connection.py    # Gestionnaire de connexion
│       └── config.py           # Configuration des variables d'environnement
├── data/                       # Stockage des données
│   ├── raw/                    # Données sources (store.csv)
│   ├── processed/              # Résultats du nettoyage et graphiques
│   └── sql_splits/             # fichiers CSV normalisés pour SQL
├── docs/                       # Documentation et livrables
│   ├── presentations/          # Supports de présentation PPTX
│   ├── img/                    # Diagrammes Merise (MCD, MLD, 3NF)
│   └── reports/                # Rapports BI générés (.docx)
├── tests/                      # Suite de tests
├── .env                        # Configuration locale (ignore par Git)
├── requirements.txt            # Liste des dépendances
└── README.md                   # Documentation principale
```

---

## Modélisation des Données (Méthode Merise)

L'architecture de la base de données repose sur une modélisation relationnelle stricte.

### 1. Modèle Conceptuel des Données (MCD)
![MCD](docs/img/mcd.png)

### 2. Modèle Logique des Données (MLD)
![MLD](docs/img/mld.png)

### 3. Modèle Physique & Normalisation (3NF)
![3NF](docs/img/3NF.png)

---

## Installation et Configuration

### 1. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 2. Configuration
Configurez vos identifiants PostgreSQL dans le fichier `.env` à la racine :
```ini
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
DB_NAME=superstore_db
```

---

## Workflows d'Exécution

### Phase 1 : Pipeline ETL & Reporting
Traitement des données brutes, calcul des KPIs et génération du rapport Word.
```bash
python main.py
```

### Phase 2 : Migration vers PostgreSQL
Normalisation des données et injection dans la base de données.
```bash
python -m src.database.db_main
```

---

## Technologies Utilisées
- **Langage :** Python 3.x
- **Manipulation de données :** Pandas
- **ORM & Database :** SQLAlchemy, PostgreSQL
- **Reporting :** Python-docx
- **Visualisation :** Matplotlib
- **Configuration :** Python-dotenv

---

## Contact
- **Développeur :** Soubi Charaf
- **Organisation :** Simplon Data Project.