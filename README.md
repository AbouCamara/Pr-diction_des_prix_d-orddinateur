# 📝 Rapport de Projet – Prédiction du Prix des Ordinateurs

## 1. 🎯 Introduction

Ce projet vise à prédire le prix d’un ordinateur portable à partir de ses caractéristiques techniques (RAM, marque, processeur, GPU, etc.).

## 2. 📊 Données utilisées

- **Source :** laptop_data.csv
- **Colonnes :** Company, CPU, RAM, SSD, GPU, Taille écran, Prix

## 3. 🧹 Prétraitement

- Suppression des unités dans les colonnes (`GB`, `inches`)
- Encodage des variables catégorielles (`pd.get_dummies`)
- Remplissage des valeurs manquantes

## 4. 🔎 Analyse exploratoire

- Histogrammes des prix
- Heatmap des corrélations
- Analyse des distributions

## 5. 🧠 Modélisation

- Modèle : Régression Linéaire
- Données divisées en jeu d'entraînement/test
- Sauvegarde des colonnes pour alignement dans Streamlit

## 6. 📈 Évaluation

- MAE, RMSE, R²
- Visualisation des performances (facultatif)

## 7. 🚀 Déploiement

- Application réalisée avec Streamlit
- Lancement local : `streamlit run app.py`

## 8. ✅ Conclusion

- Résultats satisfaisants avec la régression linéaire
- Possibilités : intégrer d'autres modèles, enrichir les données

## 9. 📎 Annexes

- `modele.pkl` : modèle entraîné
- `colonnes.pkl` : colonnes d'encodage
- `app.py` : script Streamlit
