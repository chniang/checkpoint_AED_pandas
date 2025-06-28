# 📊 Analyse exploratoire et prétraitement des données STEG (2005–2019)

Ce projet vise à réaliser une **analyse exploratoire des données (AED)** sur l’historique de facturation des clients de la Société Tunisienne d'Électricité et de Gaz (STEG), couvrant la période **2005 à 2019**.

---

## 🧠 Objectifs pédagogiques

- Charger et inspecter un jeu de données réel à grande échelle
- Identifier et gérer les valeurs manquantes
- Filtrer et extraire des sous-ensembles de données
- Réaliser une analyse descriptive des variables numériques
- Encodage de variables catégorielles (`LabelEncoder`)
- Nettoyage du `DataFrame` en supprimant les colonnes inutiles
- Préparer les données pour une analyse ou un modèle futur

---

## 📁 Fichiers du projet

| Fichier | Description |
|--------|-------------|
| `index.py` | Script principal contenant toutes les étapes d’analyse et de nettoyage |
| `STEG_BILLING_HISTORY.csv` | Données brutes de facturation (client_id, consommation, compteur, etc.) |
| `README.md` | Description du projet |

---

## 🔧 Technologies utilisées

- Python 3
- `pandas` pour la manipulation de données
- `scikit-learn` pour l’encodage de variables catégorielles (`LabelEncoder`)

---

## 🔍 Étapes réalisées

- ✔️ Chargement et exploration du fichier CSV
- ✔️ Affichage des premières lignes (`head`)
- ✔️ Inspection des types de colonnes et valeurs manquantes
- ✔️ Suppression des lignes contenant des `NaN`
- ✔️ Analyse statistique (`describe`)
- ✔️ Sélection d’un sous-ensemble (`client_id == 'train_Client_0'`)
- ✔️ Encodage de `counter_type` → `counter_type_encoded`
- ✔️ Suppression de la colonne `counter_statue`

---

## 📊 Exemple de sortie (extrait encodé)

| counter_type | counter_type_encoded |
|--------------|----------------------|
| ELEC         | 0                    |
| GAZ          | 1                    |
| ELEC         | 0                    |

---

## ✍️ Auteur

**Cheikh Niang**  
_Étudiant en Data Science & Développement Python_

🔗 [Mon profil GitHub](https://github.com/chniang)

---

## 📝 Remarques

Ce projet est réalisé dans le cadre d’un **exercice de prétraitement de données** sur une base réelle à forte volumétrie. Il peut être enrichi par la suite avec des visualisations (`matplotlib`, `seaborn`) ou du machine learning (prévisions de consommation).

