import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="5G AI Cyber Defense",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: 700;
}
.subtitle {
    font-size: 18px;
    color: #777;
}
.section {
    font-size: 24px;
    font-weight: 600;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🛡️ 5G AI Cyber Defense</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Real-Time Cyber Attack Detection & Autonomous Defense</div>',
    unsafe_allow_html=True
)

st.markdown("---")

st.sidebar.title("⚙️ Network Traffic Input")

packet_rate = st.sidebar.number_input(
    "Packet Rate", min_value=0, value=7000
)

packet_size = st.sidebar.number_input(
    "Packet Size", min_value=0, value=100
)

connection_count = st.sidebar.number_input(
    "Connection Count", min_value=0, value=1200
)

failed_connections = st.sidebar.number_input(
    "Failed Connections", min_value=0, value=900
)

traffic_duration = st.sidebar.number_input(
    "Traffic Duration", min_value=0, value=6
)

analyze = st.sidebar.button(
    "🔍 Analyze Traffic",
    use_container_width=True
)

if analyze:

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

        st.markdown(
            '<div class="section">🎯 Detection Result</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Detected Attack",
                result["prediction"].upper()
            )

        with col2:
            st.metric(
                "Confidence",
                f'{result["confidence"]}%'
            )

        with col3:
            st.metric(
                "Severity",
                result["severity"]
            )

        with col4:
            st.metric(
                "Source",
                result["source"]
            )

        st.markdown("---")

        st.markdown(
            '<div class="section">🛡️ Autonomous Defense</div>',
            unsafe_allow_html=True
        )

        st.info(result["defense_action"])

        if result["severity"] == "Critical":
            st.error("🚨 CRITICAL THREAT DETECTED")

        elif result["severity"] == "High":
            st.warning("⚠️ HIGH THREAT DETECTED")

        elif result["severity"] == "Medium":
            st.warning("⚠️ MEDIUM THREAT DETECTED")

        else:
            st.success("✅ NETWORK TRAFFIC IS NORMAL")

    except Exception as e:

        st.error(
            "Unable to connect to the FastAPI server."
        )

        st.write(e)


st.markdown("---")

st.markdown(
    '<div class="section">📊 Security Overview</div>',
    unsafe_allow_html=True
)

try:

    logs_response = requests.get(
        "http://127.0.0.1:8000/logs"
    )

    logs_data = logs_response.json()["logs"]

    if logs_data:

        total_events = len(logs_data)

        critical_count = sum(
            1 for log in logs_data
            if log[4] == "Critical"
        )

        high_count = sum(
            1 for log in logs_data
            if log[4] == "High"
        )

        medium_count = sum(
            1 for log in logs_data
            if log[4] == "Medium"
        )

        attack_types = set(
            log[2]
            for log in logs_data
            if log[2] != "normal"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Events",
                total_events
            )

        with col2:
            st.metric(
                "🔴 Critical",
                critical_count
            )

        with col3:
            st.metric(
                "🟠 High",
                high_count
            )

        with col4:
            st.metric(
                "🎯 Attack Types",
                len(attack_types)
            )

        st.markdown("---")

        st.subheader("📈 Attack Type Distribution")

        attack_counts = {}

        for log in logs_data:

            attack = log[2]

            if attack != "normal":

                attack_counts[attack] = (
                    attack_counts.get(attack, 0) + 1
                )

        if attack_counts:

            chart_data = pd.DataFrame(
                list(attack_counts.items()),
                columns=["Attack Type", "Count"]
            )

            st.bar_chart(
                chart_data,
                x="Attack Type",
                y="Count"
            )

        else:

            st.info("No attacks detected yet.")

        st.subheader("🚨 Severity Distribution")

        severity_counts = {
            "Critical": critical_count,
            "High": high_count,
            "Medium": medium_count
        }

        severity_data = pd.DataFrame(
            list(severity_counts.items()),
            columns=["Severity", "Count"]
        )

        st.bar_chart(
            severity_data,
            x="Severity",
            y="Count"
        )

        st.markdown("---")

        st.subheader("📋 Attack History")

        history = []

        for log in logs_data:

            history.append({
                "ID": log[0],
                "Timestamp": log[1],
                "Attack Type": log[2].upper(),
                "Source": (
                    log[6]
                    if len(log) > 6 and log[6]
                    else "UE-Unknown"
                ),
                "Confidence": f"{log[3]}%",
                "Severity": log[4],
                "Defense Action": log[5]
            })

        history_df = pd.DataFrame(history)

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No security events recorded yet."
        )

except Exception as e:

    st.error(
        "Unable to load security information."
    )

    st.write(e)
