import pandas as pd
import joblib

model = joblib.load("models/attack_detection_model.pkl")

FEATURES = [
    "packet_rate",
    "packet_size",
    "connection_count",
    "failed_connections",
    "traffic_duration"
]


def detect_attack(
    packet_rate,
    packet_size,
    connection_count,
    failed_connections,
    traffic_duration
):
    data = pd.DataFrame([[
        packet_rate,
        packet_size,
        connection_count,
        failed_connections,
        traffic_duration
    ]], columns=FEATURES)

    prediction = model.predict(data)[0]

    probability = max(model.predict_proba(data)[0])

    confidence = round(probability * 100, 2)

    return prediction, confidence
