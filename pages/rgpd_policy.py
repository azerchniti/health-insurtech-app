import streamlit as st

st.title("🔐 Politique de protection des données et conformité RGPD")
import streamlit as st

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter depuis la page principale.")
    st.stop()
import logging
st.markdown("---")

st.header("1. Contexte et objectifs")

st.write(
"""
Dans le cadre de ce projet **Health-InsurTech**, une application web a été développée afin de
permettre aux utilisateurs d'estimer leurs **frais médicaux annuels** grâce à un modèle
de machine learning.

Ce type d'application manipule potentiellement des **données sensibles liées à la santé**.
Il est donc essentiel de respecter les principes du **Règlement Général sur la Protection
des Données (RGPD)**.

L’approche adoptée dans ce projet repose sur le principe **Ethic-by-Design**, qui consiste
à intégrer la protection des données et les principes éthiques dès la conception du système.
"""
)

st.markdown("---")

st.header("2. Analyse d’impact – Protection des données (RGPD)")

st.write(
"""
Le jeu de données initial contient plusieurs informations personnelles
sensibles, notamment :

• nom  
• prénom  
• email  
• numéro de téléphone  
• numéro de sécurité sociale  
• adresse IP  

Ces informations permettent d’identifier directement une personne et
sont considérées comme **données personnelles sensibles** au sens du RGPD.
"""
)

st.subheader("Principe de minimisation des données")

st.write(
"""
Afin de respecter le principe de **minimisation des données**, seules les variables
strictement nécessaires à la prédiction ont été conservées.

Les variables sensibles ont été **supprimées avant l'entraînement du modèle**.

Les variables utilisées par le modèle sont uniquement :

• âge  
• sexe  
• indice de masse corporelle (IMC / BMI)  
• nombre d’enfants  
• statut fumeur  
• région  

Ces variables permettent de construire un modèle prédictif tout en limitant
l’utilisation de données personnelles.
"""
)

st.subheader("Absence de stockage des données utilisateur")

st.write(
"""
L'application ne stocke **aucune donnée personnelle saisie par l'utilisateur**.

Les informations saisies dans le formulaire de simulation sont utilisées
uniquement pour générer une **prédiction instantanée** et ne sont pas enregistrées
dans une base de données.

Cela permet de réduire considérablement les risques liés à la protection
de la vie privée.
"""
)

st.markdown("---")

st.header("3. Sécurité et gestion des accès")

st.write(
"""
Afin de limiter l'accès à l'application, un **système d'authentification simple**
a été mis en place.

L'utilisateur doit saisir :

• un nom d'utilisateur  
• un mot de passe  

avant d'accéder aux fonctionnalités de l'application.

Un système de **gestion de session** permet également de contrôler
l'accès aux différentes pages de l'application.
"""
)

st.subheader("Gestion des logs")

st.write(
"""
Un système de **journalisation (logs)** a également été implémenté dans l'application.

Les logs permettent d'enregistrer certaines actions importantes, comme :

• l'exécution d'une prédiction  
• les interactions avec l'application  

Ces informations permettent de surveiller le bon fonctionnement
du système et d'améliorer la sécurité de l'application.
"""
)

st.markdown("---")

st.header("4. Analyse des biais du modèle")

st.write(
"""
Dans le domaine de l'intelligence artificielle appliquée à la santé,
il est important d'analyser si le modèle peut introduire des **biais
dans les prédictions**.

Une analyse a été réalisée afin de vérifier si certaines catégories
d'utilisateurs étaient sur-pénalisées par le modèle.

Par exemple :

• les fumeurs  
• certaines régions  
• certaines catégories d'âge
"""
)

st.write(
"""
Les résultats montrent que certaines variables, comme le **statut fumeur**,
sont fortement corrélées avec les coûts médicaux.

Cependant, cette relation reflète une **corrélation réelle observée dans les
données médicales** et non un biais introduit par le modèle.

Afin de limiter les biais potentiels, les mesures suivantes ont été prises :

• exclusion des variables personnelles sensibles  
• utilisation d'un modèle **interprétable (régression linéaire)**  
• analyse des variables influençant la prédiction
"""
)

st.markdown("---")

st.header("5. Accessibilité – Conformité RGAA / WCAG")

st.write(
"""
L'application a été conçue pour être **accessible et compréhensible par le plus
grand nombre d'utilisateurs**, conformément aux recommandations du
**RGAA (Référentiel Général d'Amélioration de l'Accessibilité)** et du
**WCAG (Web Content Accessibility Guidelines)**.
"""
)

st.subheader("Mesures d'accessibilité mises en place")

st.write(
"""
✅ **Contraste des couleurs adapté**  
Les couleurs utilisées dans l'interface garantissent une bonne lisibilité
des textes et des éléments graphiques.

✅ **Navigation claire et structurée**  
L'application utilise une barre latérale permettant d'accéder facilement
aux différentes pages.

✅ **Interface simple et intuitive**  
Les formulaires et les graphiques sont accompagnés de titres et de
descriptions permettant une compréhension rapide de l'application.
"""
)

st.markdown("---")

st.header("6. Conclusion")

st.write(
"""
Ce projet démontre qu'il est possible d'intégrer des techniques de
**machine learning** dans une application tout en respectant les principes
de **protection des données et d'éthique numérique**.

Grâce à l'approche **Ethic-by-Design**, les données personnelles sensibles
ont été exclues du modèle et l'application garantit une utilisation
responsable de l'intelligence artificielle.
"""
)