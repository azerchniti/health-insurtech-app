
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from preprocessing import load_data
def train_model():

    df = load_data()

    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("charges", axis=1)
    y = df["charges"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    return model, score, X.columns
