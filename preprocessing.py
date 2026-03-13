
import pandas as pd

def load_data():

    df = pd.read_csv("insurance_data.csv")

    df = df[['age','sex','bmi','children','smoker','region','charges']]

    return df
