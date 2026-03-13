import streamlit as st
from model import train_model

st.set_page_config(page_title="Health Insurance Predictor", layout="wide")

# ---------- AUTHENTIFICATION ----------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:

    st.title("🔐 Connexion à l'application")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):

        if username == "test" and password == "test":
            st.session_state.authenticated = True
            st.success("Connexion réussie")
            st.rerun()
        else:
            st.error("Identifiants incorrects")

    st.stop()

# ---------- APPLICATION ----------

# Style CSS
st.markdown(
    """
    <style>
    .title {
        font-size:50px;
        font-weight:700;
        text-align:center;
        color:#2C7BE5;
    }

    .subtitle {
        font-size:20px;
        text-align:center;
        color:grey;
    }

    .section {
        font-size:26px;
        font-weight:600;
        margin-top:30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre
st.markdown('<p class="title">🏥 Health-InsurTech</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Prédiction des frais médicaux grâce au Machine Learning</p>', unsafe_allow_html=True)

st.write("")

# Charger le modèle
model, score, columns = train_model()

st.info(f"Performance du modèle (R²) : {round(score,3)}")

st.markdown("---")

# Contexte
st.markdown('<p class="section">🎯 Contexte du projet</p>', unsafe_allow_html=True)

st.write(
"""
Une compagnie d'assurance souhaite mettre à disposition de ses futurs clients 
un **outil numérique transparent** permettant d'estimer leurs **frais médicaux annuels**.

L’objectif de cette application est de permettre aux utilisateurs :

• de mieux comprendre leurs dépenses de santé potentielles  
• de choisir le **contrat d’assurance le plus adapté**  
• d'accéder à un **outil de simulation simple et accessible**

En parallèle, l’application doit garantir la **protection des données personnelles de santé**.
"""
)

st.markdown("---")

# Dataset
st.markdown('<p class="section">📊 Présentation du jeu de données</p>', unsafe_allow_html=True)

st.write(
"""
Le jeu de données utilisé dans ce projet contient **1 338 observations et 23 variables**.

Certaines variables contiennent des informations personnelles sensibles comme :

• nom  
• email  
• numéro de téléphone  
• numéro de sécurité sociale  
• adresse IP  

Afin de respecter les principes du **RGPD et de minimisation des données**, ces variables
ne sont **pas utilisées pour l'entraînement du modèle**.

Seules les variables pertinentes pour la prédiction sont conservées :

• âge  
• sexe  
• IMC (Indice de Masse Corporelle)  
• nombre d'enfants  
• statut fumeur  
• région  

🎯 **Variable cible :**

**charges** → coût médical individuel facturé par l'assurance.
"""
)

st.markdown("---")

# RGPD
st.markdown('<p class="section">⚖️ IA Éthique & Conformité RGPD</p>', unsafe_allow_html=True)

st.write(
"""
Ce projet suit une approche **Ethic-by-Design**, intégrant les principes d’éthique
et de protection des données dès la conception du système.

Les mesures mises en place sont :

✅ **Minimisation des données**  
Les données personnelles sensibles ne sont pas utilisées dans le modèle.

✅ **Transparence**  
Les variables utilisées pour la prédiction sont clairement identifiées.

✅ **Protection de la vie privée**  
Aucune donnée saisie par l’utilisateur dans l’application n’est enregistrée.

Ces mesures permettent de respecter les **principes du RGPD** tout en proposant
un système d’intelligence artificielle transparent et responsable.
"""
)

st.markdown("---")

st.info("Utilisez la barre latérale pour accéder au Dashboard et à la page de prédiction.")