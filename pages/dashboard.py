
import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data

st.title("Health Dashboard")
import streamlit as st

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter depuis la page principale.")
    st.stop()
df = load_data()

fig = px.scatter(
    df,
    x="age",
    y="charges",
    color="bmi",
    title="Age vs Medical Charges"
)

st.plotly_chart(fig)

st.dataframe(df.head())

col1, col2, col3 = st.columns(3)

col1.metric("Average BMI", round(df["bmi"].mean(),2))
col2.metric("Average Age", round(df["age"].mean(),2))
col3.metric("Average Charges", round(df["charges"].mean(),2))


corr = df.corr(numeric_only=True)

fig2 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues"
)

st.subheader("Correlation Matrix")
st.plotly_chart(fig2)