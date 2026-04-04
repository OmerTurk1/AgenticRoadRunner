import pandas as pd
from sklearn.naive_bayes import GaussianNB
import joblib

def train_model():
    df = pd.read_csv("agent_moves.csv")
    X = df.drop(columns=["action"])
    y = df["action"]
    model = GaussianNB()
    model.fit(X, y)
    print("Model trained with agent_moves.csv")
    print(f"Model accuracy on training data: {model.score(X, y):.2f}")
    joblib.dump(model, "agent_model.pkl")

if __name__ == "__main__":
    train_model()