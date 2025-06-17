"""
***********************************************************************
************** Author:   Christian KEMGANG NGUESSOP *******************
************** Project:   churn-insight             *******************
************** Version:  1.0.0                      *******************
***********************************************************************
"""

import streamlit as st


# Fonction pour afficher la page d'accueil du projet Churn Prediction
def show_home():

    # Titre principal
    st.title("📉 Bienvenue sur Churn-Insight")

    st.markdown(
        """
        <p style="text-align: left; padding-left: 5%; font-size: 20px; color: #7F8C8D; font-weight: bold;">
            Anticipez les départs de vos abonnés grâce à la puissance de la data.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Description générale du projet
    st.markdown(
        """
        **Churn-Insight** est une solution d'analyse prédictive destinée aux entreprises par abonnement.  
        Elle vous aide à **identifier les clients à risque de résiliation** avant qu’ils ne quittent votre service, grâce à un modèle de machine learning entraîné sur des données clients clés.

        ### Notre mission
        Aider les équipes marketing, produit et service client à **réduire le taux de churn**, améliorer la fidélité et personnaliser les actions de rétention.
        """
    )

    # Fonctionnalités clés
    st.header("🧠 Fonctionnalités clés")
    st.markdown(
        """
        1. **Prédiction du churn client**  
           Un modèle intelligent identifie automatiquement les clients les plus susceptibles de résilier, basé sur des facteurs comme la satisfaction, l'ancienneté, le revenu, etc.

        2. **Analyse des profils à risque**  
           Obtenez des insights sur les segments de clients les plus vulnérables, et comprenez les comportements qui précèdent une résiliation.

        3. **Visualisations interactives**  
           Explorez les variables influentes (score de satisfaction, fréquence d'utilisation, support contacté...) via des graphiques clairs et interactifs.

        4. **Explicabilité des décisions (SHAP)**  
           Chaque prédiction peut être expliquée de manière transparente, pour comprendre *pourquoi* un client est considéré à risque.

        5. **Recommandations marketing**  
           Suggestions d’actions ciblées pour les clients à risque : offres spéciales, relances automatiques, enquêtes de satisfaction.
        """
    )

    # Pourquoi Churn-Insight
    st.header("Pourquoi Churn-Insight ?")
    st.markdown(
        """
        - **Réduction du taux de résiliation** : Agissez avant qu'il ne soit trop tard, en ciblant les clients fragiles avec des campagnes adaptées.
        - **Décisions basées sur les données** : Comprenez les causes profondes du churn, et alignez vos décisions sur les données réelles.
        - **Amélioration continue** : Adaptez votre stratégie de rétention au fil du temps grâce à des modèles mis à jour régulièrement.
        """
    )

    # Données utilisées
    st.header("📊 Données utilisées")
    st.markdown(
        """
        Le modèle est entraîné sur des données clients incluant :
        - **Âge, revenu, sexe**
        - **Ancienneté, fréquence d’utilisation du service**
        - **Contact avec le support**
        - **Score de satisfaction**
        
        Ces données sont nettoyées, normalisées, et intégrées dans un pipeline d’analyse automatique.
        """
    )

    # Footer
    st.header("📞 Contact & Mentions Légales")
    st.markdown(
        """
        - Pour toute question, contactez-nous à : [support@churn-insight.ai](mailto:contact@chagest.com)  
        - **Mentions légales** : Cette application est une démonstration pédagogique basée sur des données simulées pour illustrer des cas d’usage en data science.
        
        Version 1.0 | Copyright © 2025
        """
    )
