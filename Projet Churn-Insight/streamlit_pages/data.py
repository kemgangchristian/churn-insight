"""
***********************************************************************
************** Author:   Christian KEMGANG NGUESSOP *******************
************** Project:   churn-insight             *******************
************** Version:  1.0.0                      *******************
***********************************************************************
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def show_data():

    st.title("📁 Exploration des Données Clients")

    # Charger les données
    df = pd.read_csv("churn_clients.csv")

    # Nettoyage des noms de colonnes
    df.columns = df.columns.str.strip().str.replace("é", "e").str.replace("É", "E")

    # Afficher un aperçu du DataFrame
    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    # Nombre de clients
    st.markdown(f"**Nombre total de clients** : {df.shape[0]}")
    st.markdown(f"**Nombre de variables** : {df.shape[1]}")

    # Afficher les colonnes disponibles
    st.markdown("**Colonnes disponibles :**")
    st.write(df.columns.tolist())

    # Statistiques descriptives
    st.subheader("📈 Statistiques descriptives")
    st.write(df.describe())

    # Section des valeurs manquantes
    st.subheader("🔍 Valeurs manquantes")
    # Calcul des valeurs manquantes pour chaque colonne
    missing_values = df.isnull().sum()
    # Créer un DataFrame pour les valeurs manquantes
    missing_df = pd.DataFrame(
        {"Colonne": missing_values.index, "Valeurs manquantes": missing_values.values}
    )
    # Trier les colonnes par nombre de valeurs manquantes (si nécessaire)
    missing_df = missing_df.sort_values(by="Valeurs manquantes", ascending=False)
    # Affichage du tableau avec un style
    st.write(
        missing_df.style.format(
            {
                "Valeurs manquantes": "{:,.0f}"  # Format des valeurs manquantes sans décimale
            }
        ).background_gradient(
            cmap="Blues", subset=["Valeurs manquantes"]
        )  # Dégradé de couleur
    )

    # Créer deux colonnes côte à côte
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎂 Répartition de l'âge")
        fig1, ax1 = plt.subplots()
        sns.histplot(df["Age"], kde=True, bins=20, color="skyblue", ax=ax1)
        ax1.set_ylim(10, ax1.get_ylim()[1])
        st.pyplot(fig1)

    with col2:
        st.subheader("💰 Répartition du revenu")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["Revenu"], kde=True, bins=20, color="orange", ax=ax2)
        ax2.set_ylim(10, ax2.get_ylim()[1])
        st.pyplot(fig2)

    # Boxplot Score de satisfaction vs Résiliation
    st.subheader("📦 Satisfaction selon la résiliation")
    if "Resilie" in df.columns and "Score_satisfaction" in df.columns:
        fig3, ax3 = plt.subplots()
        sns.boxplot(
            data=df,
            x="Resilie",
            y="Score_satisfaction",
            hue="Resilie",
            palette="Set2",
            ax=ax3,
            legend=False,
        )

        # Définir les labels X si les valeurs sont 0 / 1
        if set(df["Resilie"].unique()) == {0, 1}:
            ax3.set_xticks([0, 1])
            ax3.set_xticklabels(["Non Résilié", "Résilié"])

        ax3.set_title("Score de satisfaction selon la résiliation")
        st.pyplot(fig3)
    else:
        st.warning(
            "Colonne 'Resilie' ou 'Score_satisfaction' introuvable dans le dataset."
        )

    # Corrélation avec la variable cible
    st.subheader("📊 Corrélations avec la résiliation")
    if "Resilie" in df.columns:
        corr = df.corr(numeric_only=True)
        if "Resilie" in corr.columns:
            st.write(corr["Resilie"].sort_values(ascending=False))
        else:
            st.warning("Pas de corrélation calculable avec la colonne 'Resilie'")
    else:
        st.warning("Colonne 'Resilie' manquante.")
