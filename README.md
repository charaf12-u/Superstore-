# Préparation et Transformation des Données Ventes

Ce projet est une solution automatisée pour le traitement, l'analyse et la visualisation des données de ventes d'un Superstore. Il permet de transformer des données brutes en un rapport d'analyse complet au format Word.

## 🚀 Fonctionnalités

- **Nettoyage Automatisé** : Suppression des doublons, correction des colonnes et gestion des valeurs manquantes.
- **Transformations de Données** : Extraction temporelle (mois, année), calcul de marges et délais de livraison.
- **Analyse des Valeurs Aberrantes** : Détection des anomalies via la méthode IQR.
- **Visualisations Dynamiques** : Graphiques de ventes par catégorie, région, segment, et évolution mensuelle.
- **Génération de Rapport** : Exportation des résultats dans un document Word (`.docx`) prêt à l'emploi.

## 📁 Structure du Projet

```text
📦 Superstore Data Project
├── 🚀 main.py                     # Point d'entrée de l'application
├── 📂 fichier_py/                 # Code source Python
│   ├── 🛠️ read_clean_data.py      # Script principal de traitement
│   ├── 🔧 fun.py                  # Fonctions utilitaires (typage)
│   ├── 📈 graphes.py              # Génération des graphiques
│   └── 📄 rapport.py              # Génération du rapport Word
├── 📁 fichier_data/               # Dossier contenant la source (store.csv)
├── 📂 fichier_livrable/           # Dossier de sortie (CSV nettoyé et Rapport)
└── 🗄️ PostgreSQL/                 # Intégration et gestion de la base de données
    ├── 🚀 main.py                 # Point d'entrée pour l'exécution des scripts BDD
    ├── 📜 scripts/                # Scripts SQL et Python pour la BDD
    │   ├── ⚙️ config.py           # Configuration de la connexion à PostgreSQL
    │   ├── 🏗️ create_tables.py    # Création du schéma relationnel
    │   ├── ✂️ split_csv.py        # Découpage du CSV nettoyé pour l'insertion
    │   ├── 📥 insert_data.py      # Insertion automatique des données
    │   └── 🔍 check_uniqueness.py # Vérification des doublons
    └── 🧪 tests/                  # Scripts de tests unitaires
        ├── 🔌 test_connection.py  # Test de la connexion à la base de données
        ├── 📝 test_insertion.py   # Test du bon déroulement de l'insertion
        └── 🔎 test_queries.py     # Test de l'exécution de requêtes SQL
```

## 🛠️ Installation

1. Assurez-vous d'avoir Python 3.x installé.
2. Installez les dépendances nécessaires :
   ```bash
   pip install pandas matplotlib python-docx
   ```

## 💻 Utilisation

Placez votre fichier `store.csv` dans le dossier `fichier_data/`, puis lancez le script principal :

```powershell
python main.py
```

Les résultats seront générés dans le dossier `fichier_livrable/` :
- `superstore_clean.csv` : Les données nettoyées.
- `rapport.docx` : Le rapport final avec graphiques.

### 🗄️ Base de Données (PostgreSQL)

Une fois les données brutes nettoyées, vous pouvez les intégrer dans une base de données PostgreSQL en utilisant le module inclus.

**Comment l'utiliser ?**
1. Configurez vos identifiants pour la base de données dans le fichier `PostgreSQL/scripts/config.py`.
2. Déplacez-vous dans le dossier `PostgreSQL` et lancez son script d'exécution principal :

```powershell
cd PostgreSQL
python main.py
```

**Que fait ce script ?**
Il va exécuter automatiquement dans l'ordre les opérations suivantes :
- **Création des tables** (`create_tables.py`) : Prépare la structure (Client, Produit, Commande, etc.) dans votre base de données.
- **Découpage des données** (`split_csv.py`) : Prépare et divise le fichier CSV pour optimiser l'insertion.
- **Insertion Automatique** (`insert_data.py`) : Intègre les données propres dans les différentes tables de la base.
- **Contrôle d'intégrité** (`check_uniqueness.py`) : Vérifie qu'il n'y a pas de doublons créés lors de l'insertion.

Des scripts de tests (connexion, requêtes) se trouvent également dans le dossier `PostgreSQL/tests/` pour vérifier que tout fonctionne bien à chaque étape.

## 📊 Technologies Utilisées

- **Pandas** : Pour la manipulation et le nettoyage des données brutes.
- **Matplotlib** : Pour la création de visualisations et graphiques détaillés.
- **Python-docx** : Pour la génération automatisée et stylisée de rapports Word.
- **PostgreSQL** : Système de gestion de base de données relationnelle pour le stockage sécurisé.
- **Psycopg2** : Adaptateur PostgreSQL pour Python, utilisé pour les requêtes SQL.
- **Unittest** : Framework Python intégré pour tester la base de données.
