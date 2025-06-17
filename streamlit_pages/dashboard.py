"""
***********************************************************************
************** Author:   Christian KEMGANG NGUESSOP *******************
************** Project:   churn-insight             *******************
************** Version:  1.0.0                      *******************
***********************************************************************
"""

import streamlit as st
import joblib
import pandas as pd


def show_dashboard():
    # Charger le modèle et le scaler
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")

    # Titre principal
    st.markdown(
        "<h1 style='text-align: center;'>📊 Dashboard de Prédiction de Résiliation</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "#### Analysez et anticipez le risque de départ d’un client",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # ----------------------------
    # Saisie utilisateur
    # ----------------------------
    st.header("🧾 Informations Client")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("🎂 Âge", 18, 100, 30)
        revenu = st.number_input("💶 Revenu mensuel (€)", 1000, 10000, 5000, step=100)
        sexe = st.selectbox("🧍 Sexe", ["Femme", "Homme"])
        support = st.selectbox("📞 A contacté le support ?", ["Non", "Oui"])

    with col2:
        anciennete = st.slider("📅 Ancienneté (années)", 0, 10, 2)
        frequence = st.slider("📈 Fréquence d'utilisation (par mois)", 0, 30, 10)
        score = st.slider("⭐ Score de satisfaction (1 à 10)", 1, 10, 5)

    st.markdown("---")

    # ----------------------------
    # Prédiction
    # ----------------------------
    if st.button("🔍 Lancer la prédiction"):
        # Créer un DataFrame
        input_data = pd.DataFrame(
            {
                "Age": [age],
                "Revenu": [revenu],
                "Sexe": [1 if sexe == "Homme" else 0],
                "Anciennete": [anciennete],
                "Frequence_utilisation": [frequence],
                "Support_contacte": [1 if support == "Oui" else 0],
                "Score_satisfaction": [score],
            }
        )

        # Normalisation des colonnes numériques
        num_cols = ["Age", "Revenu", "Anciennete", "Frequence_utilisation"]
        input_data[num_cols] = scaler.transform(input_data[num_cols])

        # Prédiction
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]

        # Affichage du résultat
        st.subheader("📢 Résultat de la prédiction")
        if prediction == 1:
            st.error("⚠️ Risque de résiliation **ÉLEVÉ**")
        else:
            st.success("✅ Risque de résiliation **FAIBLE**")

        st.metric(label="📊 Probabilité estimée", value=f"{proba:.2%}")
