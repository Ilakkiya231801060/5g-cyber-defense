def get_severity(attack_type, confidence):
    if attack_type == "normal":
        return "None"

    if attack_type in ["ddos", "dos"]:
        return "Critical" if confidence >= 90 else "High"

    if attack_type in ["brute_force", "web_attack", "infiltration"]:
        return "High" if confidence >= 75 else "Medium"

    if attack_type in ["port_scan", "botnet"]:
        return "High" if confidence >= 90 else "Medium"

    if attack_type == "unknown_anomaly":
        return "High" if confidence >= 80 else "Medium"

    return "Medium"


def identify_source(packet_rate, connection_count, failed_connections):
    if connection_count > 1000:
        return "UE-High-Traffic"

    if failed_connections > 500:
        return "UE-Suspicious"

    if connection_count > 500:
        return "UE-Multiple-Connections"

    return "UE-Unknown"


def take_defense_action(attack_type):
    if attack_type in ["ddos", "dos"]:
        return "Traffic blocked - source isolated"

    elif attack_type in ["brute_force", "web_attack"]:
        return "Suspicious source blocked - access restricted"

    elif attack_type in ["port_scan", "botnet"]:
        return "Source isolated - suspicious connections blocked"

    elif attack_type == "infiltration":
        return "Device isolated - security monitoring enabled"

    elif attack_type == "unknown_anomaly":
        return "Unknown anomaly detected - source isolated for monitoring"

    else:
        return "Normal traffic - no defense action required"


def analyze_security_event(
    attack_type,
    confidence,
    packet_rate,
    connection_count,
    failed_connections
):
    severity = get_severity(attack_type, confidence)

    source = identify_source(
        packet_rate,
        connection_count,
        failed_connections
    )

    defense = take_defense_action(attack_type)

    return {
        "attack_type": attack_type,
        "confidence": confidence,
        "severity": severity,
        "source": source,
        "defense_action": defense
    }


if __name__ == "__main__":
    result = analyze_security_event(
        "ddos",
        95,
        8000,
        1200,
        800
    )

    print("Attack Type:", result["attack_type"])
    print("Confidence:", result["confidence"], "%")
    print("Severity:", result["severity"])
    print("Source:", result["source"])
    print("Defense:", result["defense_action"])
