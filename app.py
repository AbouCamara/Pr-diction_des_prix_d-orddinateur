import streamlit as st
import pandas as pd
import joblib

# Charger modèle et colonnes
model = joblib.load("modele.pkl")
expected_columns = joblib.load("colonnes.pkl")  # liste des colonnes utilisées à l'entraînement

# Interface utilisateur
company = st.selectbox("Marque (Company)", ["HP", "Apple", "Acer", "Asus", "Dell", "Lenovo"])
cpu = st.selectbox("Processeur (CPU)", [
    "Intel Core i5 7200U 2.5GHz",
    "Intel Core i7 8550U 1.8GHz",
    "AMD A12-Series 9700P 2.5GHz",
    "Intel Core i3 6006U 2.0GHz",
])
ram = st.number_input("RAM (Go)", 4, 64, 8)
ssd = st.number_input("Stockage SSD (Go)", 128, 2048, 512)
gpu = st.selectbox("Carte graphique dédiée ?", ["Oui", "Non"])
screen = st.slider("Taille écran (pouces)", 11.0, 17.0, 15.6)

# Création DataFrame utilisateur
input_df = pd.DataFrame([{
    "Company": company,
    "Cpu": cpu,
    "Ram": ram,
    "SSD": ssd,
    "GPU": gpu,
    "screen_size": screen
}])

# Encodage identique à l'entraînement
input_encoded = pd.get_dummies(input_df)

# Alignement avec les colonnes attendues par le modèle
input_encoded = input_encoded.reindex(columns=expected_columns, fill_value=0)

# Prédiction
if st.button("Prédire le prix"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"💰 Prix estimé : {round(prediction, 2)} €")
