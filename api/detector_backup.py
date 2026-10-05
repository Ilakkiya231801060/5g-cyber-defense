import pandas as pd
import joblib

model = joblib.load("models/attack_detection_model.pkl")

def detect_attack(packet_rate, packet_size, connection_count, failed_connections, traffic_duration):
    data = pd.DataFrame([[
        packet_rate,
        packet_size,
        connection_count,
        failed_connections,
        traffic_duration
    ]], columns=[
        "packet_rate",
        "packet_size",
        "connection_count",
        "failed_connections",
        "traffic_duration"
    ])

    prediction = model.predict(data)[0]
    probability = max(model.predict_proba(data)[0])

    return prediction, round(probability * 100, 2)


if __name__ == "__main__":
    result, confidence = detect_attack(400, 300, 50, 25, 40) 

    print("Detected Traffic:", result)
    print("Confidence:", confidence, "%")

