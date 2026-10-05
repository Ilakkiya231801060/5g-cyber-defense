from fastapi import FastAPI
from pydantic import BaseModel
from api.detector import detect_attack
from api.defense import take_defense_action
from database import log_attack, get_logs

app = FastAPI(title="5G Cyber Defense API")


class TrafficData(BaseModel):
    packet_rate: int
    packet_size: int
    connection_count: int
    failed_connections: int
    traffic_duration: int


@app.get("/")
def home():
    return {"message": "5G Cyber Defense API is running"}


@app.post("/detect")
def detect(data: TrafficData):

    result, confidence = detect_attack(
        data.packet_rate,
        data.packet_size,
        data.connection_count,
        data.failed_connections,
        data.traffic_duration
    )

    if result == "ddos":
        threat_level = "Critical"
    elif result == "abnormal":
        threat_level = "High"
    else:
        threat_level = "Low"

    defense_action = take_defense_action(result)

    log_attack(
        result,
        confidence,
        threat_level,
        defense_action
    )

    return {
        "prediction": result,
        "confidence": confidence,
        "threat_level": threat_level,
        "defense_action": defense_action
    }


@app.get("/logs")
def logs():
    return {"logs": get_logs()}
