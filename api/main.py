from fastapi import FastAPI
from pydantic import BaseModel
from api.detector import detect_attack
from api.defense import analyze_security_event
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

    security_event = analyze_security_event(
        result,
        confidence,
        data.packet_rate,
        data.connection_count,
        data.failed_connections
    )

    log_attack(
        security_event["attack_type"],
        security_event["source"],
        security_event["confidence"],
        security_event["severity"],
        security_event["defense_action"]
    )

    return {
        "prediction": security_event["attack_type"],
        "confidence": security_event["confidence"],
        "severity": security_event["severity"],
        "source": security_event["source"],
        "defense_action": security_event["defense_action"]
    }


@app.get("/logs")
def logs():
    return {"logs": get_logs()}
