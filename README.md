# neurips2025-arc

# 🧩 NeurIPS 2025 - Google Code Golf Championship

## 🚀 Description
Ce projet participe à la compétition **NeurIPS 2025 - Google Code Golf Championship** (ARC-AGI challenge).  
L’objectif est de produire une suite de programmes Python minimalistes capables de résoudre les 400 tâches du benchmark ARC-AGI.


## 📂 Structure du projet
neurips2025/
│── data/ # Datasets (task001.json, …)
│── solutions/ # Scripts Python (task001.py, …)
│── utils/ # Fonctions utilitaires
│── notebooks/ # Analyses exploratoires Jupyter
│── tests/ # Scripts de test et validation
│── README.md # Documentation principale
│── requirements.txt # Dépendances du projet

bash
Copier
Modifier

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/<TON-USER>/<TON-REPO>.git
cd <TON-REPO>
2. Créer un environnement virtuel
bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate   # sous Linux/Mac
venv\Scripts\activate      # sous Windows


3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt

▶️ Utilisation
Lancer un script de solution
bash
Copier
Modifier
python solutions/task001.py
Tester toutes les solutions
bash
Copier
Modifier
python tests/run_all.py


📊 Résultats attendus
✅ Chaque programme doit résoudre correctement les exemples train et test.

✅ Les solutions doivent être les plus courtes possible (Code Golf).

✅ Les résultats sont validés sur Kaggle (NeurIPS 2025).

