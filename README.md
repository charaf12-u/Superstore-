# 📊 Superstore Data Lifecycle: ETL to PostgreSQL & Reporting

Ce projet fournit une solution automatisée de bout en bout pour le **cycle de vie des données de vente Superstore**. Il couvre l'ensemble du pipeline : de l'ingestion et du nettoyage des données brutes (ETL) à l'intégration d'une base de données relationnelle (PostgreSQL) et à la génération de rapports d'analyse au format Word.

---

## 📁 Structure du Projet (Nouvelle Organisation)

```text
📦 Superstore-Project
├── 🚀 main.py                     # Point d'entrée principal du pipeline
├── 📂 src/                        # Logique métier (ETL, Visualisation, Reporting)
│   ├── 📂 cleaning/               # Nettoyage et transformation (read_clean_data.py, fun.py)
│   ├── 📂 visual/                 # Moteur de visualisation (graphes.py)
│   ├── 📂 reporting/              # Génération de rapport Word (rapport.py)
│   └── 📂 database/               # Gestion de la base de données PostgreSQL
├── 📂 data/                       # Entrepôt de données
│   ├── 📥 raw/                    # Données brutes (store.csv)
│   └── 📤 processed/              # Données nettoyées et graphiques temporaires
├── 📂 docs/                       # Documentation et livrables
│   ├── 📊 presentations/          # Présentations PPTX
│   └── 📄 reports/                # Rapports finaux (.docx)
├── 🧪 tests/                      # Suite de tests
├── 📄 requirements.txt            # Dépendances Python
└── 📄 README.md                   # Documentation du projet
```

---

## 🚀 Fonctionnalités Clés

*   **Nettoyage Automatisé (ETL) :** Gestion des doublons, valeurs manquantes et corrections de types.
*   **Analyses Avancées :** Calcul de marges, délais de livraison et tendances de ventes.
*   **Détection d'Anomalies :** Identification des valeurs aberrantes via la méthode IQR.
*   **Reporting Dynamique :** Génération automatique de rapports Word (`.docx`) avec graphiques intégrés.

---

## ⚙️ Installation et Utilisation

### 1. Installation
Assurez-vous d'avoir Python 3.8+ installé, puis exécutez :
```bash
pip install -r requirements.txt
```

### 2. Exécution du Pipeline
Placez votre fichier `store.csv` dans `data/raw/` et lancez le script principal :
```bash
python main.py
```

---

## 📧 Contact
- **Auteur :** Soubi Charaf (Reorganisé par Antigravity)
- **Projet :** Simplon Data Project
