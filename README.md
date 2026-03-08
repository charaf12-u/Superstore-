# 📊 Superstore Data Lifecycle: ETL to PostgreSQL & Reporting

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/database-PostgreSQL-336791.svg)](https://www.postgresql.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

## 📝 Project Overview
This project provides an end-to-end automated solution for the **Superstore sales data lifecycle**. It covers the entire pipeline: from raw data ingestion and cleaning (ETL) to relational database integration (PostgreSQL) and the generation of professional business intelligence reports.

---

## 🚀 Key Features

*   **Automated Data Cleaning (ETL):** Intelligent handling of duplicates, missing values, and data type corrections.
*   **Advanced Analytics:** Calculation of business metrics such as profit margins, shipping delays, and multi-dimensional sales trends.
*   **Outlier Detection:** Statistical anomaly detection using the Interquartile Range (IQR) method.
*   **Relational Database Mapping:** A robust PostgreSQL schema designed to normalize flat CSV data into a structured relational model.
*   **Dynamic Data Splitting:** Intelligent scripts to prepare and split cleaned data for bulk database insertion.
*   **Reporting Engine:** Automatic generation of high-quality Word (`.docx`) reports containing data-driven insights and visualizations.
*   **Comprehensive Testing:** Integrated test suite for database connectivity, data integrity, and analytical accuracy.

---

## 📁 Project Architecture

```text
📦 Superstore-Project
├── 🚀 main.py                     # Entry point for the ETL & Reporting pipeline
├── 📂 fichier_py/                 # Core Python Logic (ETL & Analysis)
│   ├── 🛠️ read_clean_data.py      # Main processing & cleaning logic
│   ├── 🔧 fun.py                  # Utility functions (typing & formatting)
│   ├── 📈 graphes.py              # Data visualization engine (Matplotlib)
│   └── 📄 rapport.py              # Word report generation logic
├── 📁 fichier_data/               # Raw Data Source (store.csv)
├── 📂 fichier_livrable/           # Final Output (Cleaned CSV & Business Report)
├── 📂 PostgreSQL/                 # Database Integration Layer
│   ├── 🚀 main.py                 # Main execution script for Database operations
│   ├── 📜 scripts/                # Database Management Scripts
│   │   ├── ⚙️ config.py           # Database connection parameters
│   │   ├── 🏗️ create_tables.py    # SQL Schema definition & table creation
│   │   ├── ✂️ split_csv.py        # logic to normalize & split data into tables
│   │   ├── 📥 insert_data.py      # Automated bulk data insertion logic
│   │   └── 🔍 check_uniqueness.py # Data integrity & uniqueness validation
│   └── 🧪 tests/                  # Verification Suite
│       ├── 📊 test_analytics.py   # Analysis & query results verification
│       └── 📝 test_insertion.py   # Insertion & Join relational testing
└── 📄 README.md                   # Project Documentation
```

---

## 🛠️ Technical Stack

| Component | Technology | Use Case |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core logic and automation |
| **Data Manipulation** | Pandas / NumPy | ETL, cleaning, and transformation |
| **Visualization** | Matplotlib / Seaborn | Chart generation for reports |
| **Reporting** | Python-docx | Professional document generation |
| **Database** | PostgreSQL | Scalable storage & relational management |
| **Database Driver** | Psycopg2 / SQLAlchemy | Python-PostgreSQL communication |
| **Testing** | Unittest / PyTest | Ensuring code and data reliability |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** and a **PostgreSQL** instance running.

### 2. Environment Setup
Clone the repository and install the dependencies:
```bash
# Install core dependencies
pip install pandas matplotlib python-docx psycopg2 sqlalchemy
```

### 3. Database Configuration
Edit `PostgreSQL/scripts/config.py` with your database credentials:
```python
DB_CONFIG = {
    "host": "localhost",
    "database": "superstore_db",
    "user": "your_user",
    "password": "your_password"
}
```

---

## 💻 Workflow Execution

### Phase 1: Data Processing & Reporting
Place your raw `store.csv` in `fichier_data/` and run the main engine:
```powershell
python main.py
```
> **Output:** Review the cleaned data and the generated `.docx` report in `fichier_livrable/`.

### Phase 2: Database Migration
To migrate the cleaned data into PostgreSQL:
```powershell
cd PostgreSQL
python main.py
```
This script handles the sequence of:
1.  **Schema Creation**: Building the relational structure.
2.  **Data Normalization**: Splitting the CSV into normalized tables.
3.  **Bulk Insertion**: Populating the database.
4.  **Integrity Check**: Verifying uniqueness and foreign keys.

### Phase 3: Verification
Run the test suite to ensure everything is perfect:
```powershell
python -m unittest discover PostgreSQL/tests
```

---

## 📊 Database Schema Overview
The project transforms a flat CSV into a normalized relational model including:
- **Core Entities:** `Client`, `Produit`, `Date_Temps`, `Localisation`.
- **Relational Links:** `Region` → `Etat` → `Localisation`.
- **Transactional Data:** `Commande` and `Ventes` (acting as a fact table).

---

## 📧 Contact & Contribution
- **Author:** Soubi Charaf
- **Contribution:** Pull requests are welcome! For major changes, please open an issue first.

---
*Created with ❤️ for the Simplon Data Project.*
