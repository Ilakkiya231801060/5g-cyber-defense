import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("data/network_traffic.csv")

features = [
    "packet_rate",
    "packet_size",
    "connection_count",
    "failed_connections",
    "traffic_duration"
]

X = data[data["label"] == "normal"][features]

model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

model.fit(X)

joblib.dump(model, "models/anomaly_detector.pkl")

print("Anomaly Detection Model Created!")
print("Training samples:", len(X))
print("Model saved successfully!")
