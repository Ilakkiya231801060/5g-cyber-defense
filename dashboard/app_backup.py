import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="5G Cyber Defense",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI-Based 5G Cyber Defense")
st.subheader("Real-Time Cyber Attack Detection & Autonomous Defense")

st.sidebar.header("Network Traffic")

packet_rate = st.sidebar.number_input("Packet Rate", min_value=0, value=7000)
packet_size = st.sidebar.number_input("Packet Size", min_value=0, value=100)
connection_count = st.sidebar.number_input("Connection Count", min_value=0, value=1200)
failed_connections = st.sidebar.number_input("Failed Connections", min_value=0, value=900)
traffic_duration = st.sidebar.number_input("Traffic Duration", min_value=0, value=6)

if st.sidebar.button("Analyze Traffic"):

    data = {
        "packet_rate": packet_rate,
        "packet_size": packet_size,
        "connection_count": connection_count,
        "failed_connections": failed_connections,
        "traffic_duration": traffic_duration
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/detect",
            json=data
        )

        result = response.json()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Detected Attack", result["prediction"].upper())

        with col2:
            st.metric("Confidence", f'{result["confidence"]}%')

        with col3:
            st.metric("Severity", result["severity"])

        with col4:
            st.metric("Source", result["source"])

        st.subheader("🛡️ Autonomous Defense")
        st.info(result["defense_action"])

        if result["severity"] == "Critical":
            st.error("🚨 CRITICAL THREAT DETECTED")
        elif result["severity"] == "High":
            st.warning("⚠️ HIGH THREAT DETECTED")
        elif result["severity"] == "Medium":
            st.warning("⚠️ MEDIUM THREAT DETECTED")
        else:
            st.success("✅ Network Traffic is Normal")

    except Exception as e:
        st.error("Unable to connect to the FastAPI server.")
        st.write(e)


st.subheader("📊 Security Overview")

try:
    logs_response = requests.get(
        "http://127.0.0.1:8000/logs"
    )

    logs_data = logs_response.json()["logs"]

    total_attacks = sum(
        1 for log in logs_data if log[2] != "normal"
    )

    attack_types = {}

    for log in logs_data:
        attack = log[2]
        if attack != "normal":
            attack_types[attack] = attack_types.get(attack, 0) + 1

    critical_attacks = sum(
        1 for log in logs_data if log[4] == "Critical"
    )

    high_attacks = sum(
        1 for log in logs_data if log[4] == "High"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Attacks", total_attacks)

    with col2:
        st.metric("Critical", critical_attacks)

    with col3:
        st.metric("High", high_attacks)

    with col4:
        st.metric("Attack Types", len(attack_types))

    st.subheader("📈 Attack Type Distribution")

    if attack_types:
        chart_data = pd.DataFrame(
            list(attack_types.items()),
            columns=["Attack Type", "Count"]
        )

        st.bar_chart(
            chart_data,
            x="Attack Type",
            y="Count"
        )
    else:
        st.info("No attacks detected yet.")

    st.subheader("📋 Attack History")

    if logs_data:

        history = []

        for log in logs_data:
            history.append({
                "ID": log[0],
                "Timestamp": log[1],
                "Attack Type": log[2].upper(),
                "Source": log[6] if log[6] else "Unknown",
                "Confidence": f"{log[3]}%",
                "Severity": log[4],
                "Defense Action": log[5]
            })

        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No attack records found.")

except Exception as e:
    st.error("Unable to load attack history.")
    st.write(e)
