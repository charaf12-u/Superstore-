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
├── main.py                     # Point d'entrée de l'application
├── fichier_py/                 # Code source Python
│   ├── read_clean_data.py      # Script principal de traitement
│   ├── fun.py                  # Fonctions utilitaires (typage)
│   ├── graphes.py              # Génération des graphiques
│   └── rapport.py              # Génération du rapport Word
├── fichier_data/               # Dossier contenant la source (store.csv)
└── fichier_livrable/           # Dossier de sortie (CSV nettoyé et Rapport)
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

## 📊 Technologies Utilisées

- **Pandas** : Pour la manipulation et le nettoyage des données.
- **Matplotlib** : Pour la création des graphiques.
- **Python-docx** : Pour la génération automatisée de documents Word.
