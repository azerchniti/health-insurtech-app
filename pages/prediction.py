import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from model import train_model

st.title("Predict Medical Costs")
import streamlit as st

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter depuis la page principale.")
    st.stop()
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# train model
model, score, columns = train_model()

# Sidebar inputs
st.sidebar.header("User Information")

age = st.sidebar.slider("Age", 18, 80, 30)
bmi = st.sidebar.slider("BMI", 15.0, 40.0, 25.0)
children = st.sidebar.slider("Children", 0, 5, 0)

sex = st.sidebar.selectbox("Sex", ["male", "female"])
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# create dataframe
input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "sex": [sex],
    "smoker": [smoker],
    "region": [region]
})

# encode categorical variables
input_data = pd.get_dummies(input_data)

# align columns with training data
for col in columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[columns]

# prediction button
if st.button("Predict cost"):
    prediction = model.predict(input_data)
    logging.info("Une prédiction a été effectuée")

    st.success(f"Estimated annual medical cost: ${round(prediction[0],2)}")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction[0],
        title={'text': "Estimated Medical Cost"},
        gauge={
            'axis': {'range': [0, 50000]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0,15000], 'color': "lightgreen"},
                {'range': [15000,30000], 'color': "orange"},
                {'range': [30000,50000], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(fig, key="cost_gauge")