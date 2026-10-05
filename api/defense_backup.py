def take_defense_action(attack_type):
    if attack_type == "ddos":
        return "DDoS detected - suspicious traffic source blocked"

    elif attack_type == "abnormal":
        return "Abnormal traffic detected - device isolated for monitoring"

    else:
        return "Normal traffic - no defense action required"


if __name__ == "__main__":
    print(take_defense_action("ddos"))
