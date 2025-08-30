# neurips2025-arc

# 🏆 NeurIPS 2025 - Google Code Golf Championship (ARC-AGI Challenge)

## 🚀 Description
e projet participe à la compétition **NeurIPS 2025 - Google Code Golf Championship**, dont l’objectif est de résoudre les **400 tâches ARC-AGI**.  
Chaque tâche doit être résolue par un **programme Python minimaliste** (Code Golf).  
Nous combinons **méthodes symboliques (ILP)** et **métaheuristiques (GA, heuristiques)** pour apprendre des règles générales et atteindre des solutions robustes et optimisées.

## 📂 Structure du projet

```text
📂 neurips2025-arc
 ┣ 📂 data         → Datasets (task001.json, …)
 ┣ 📂 solutions    → Scripts Python (task001.py, …)
 ┣ 📂 utils        → Fonctions utilitaires (helpers, primitives…)
 ┣ 📂 notebooks    → Analyses exploratoires (Jupyter)
 ┣ 📂 tests        → Validation & évaluation
 ┣ 📂 outputs      → Résultats, logs ou checkpoints
 ┣ 📄 requirements.txt   → Dépendances du projet
 ┗ 📄 README.md          → Documentation principale

``` 

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/domoesiea/neurips2025-arc.git
cd neurips2025-arc


```
### 2. Créer un environnement virtuel
``` bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


```
### 3. Installer les dépendances
``` bash
pip install -r requirements.txt
```

## ▶️ Utilisation
#### Lancer un script de solution
```bash
python solutions/task001.py
```
#### Tester toutes les solutions
```bash
python tests/run_all.py
```

### 🚀 Setup rapide
Cloner le projet et exécuter :

```bash
git clone https://github.com/domoesiea/neurips2025-arc.git
cd neurips2025-arc
./setup.sh
```

## 📊 Résultats attendus

- ✅ Chaque programme doit résoudre correctement les exemples train et test.

- ✅ Les solutions doivent être les plus courtes possible (Code Golf).

- ✅ Les résultats sont validés sur Kaggle (NeurIPS 2025).


## 🔬 Roadmap

- ✅ Le Setup du projet et environnement virtuel

- ✅ Le Solution baseline pour task001

- ⬜ LImplémentation GA pour la recherche de règles

- ⬜ Intégration ILP (Popper) pour l’induction symbolique

- ⬜ Runner générique pour tester les 400 tâches

- ⬜ Optimisation code golf



## 👥 Collaboration

- **Issues** → suivi des bugs/features  
- **Branches** → `main`, `dev`, `feature/taskXXX`  
- **Pull requests** → discussion avant merge 
