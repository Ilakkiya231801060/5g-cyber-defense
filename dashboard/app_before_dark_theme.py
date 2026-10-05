import streamlit as st
import requests
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="5G AI Cyber Defense",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# CUSTOM PROFESSIONAL STYLE
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 6px;
}

.subtitle {
    font-size: 19px;
    color: #6b7280;
    margin-bottom: 24px;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 18px;
}


/* =========================================================
   STATUS CARDS
   ========================================================= */

.status-card {
    padding: 22px;
    border-radius: 14px;
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    text-align: center;
    margin-bottom: 18px;
}

.status-title {
    font-size: 18px;
    color: #64748b;
    margin-bottom: 8px;
}

.status-value {
    font-size: 27px;
    font-weight: 700;
}


/* =========================================================
   MODEL CARDS
   ========================================================= */

.model-card {
    padding: 24px;
    border-radius: 14px;
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    min-height: 125px;
}

.model-label {
    font-size: 17px;
    color: #64748b;
}

.model-value {
    font-size: 25px;
    font-weight: 700;
    margin-top: 8px;
}


/* =========================================================
   PROTECTION CARDS
   ========================================================= */

.protection-card {
    padding: 24px;
    border-radius: 14px;
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    text-align: center;
}

.protection-active {
    font-size: 27px;
    font-weight: 700;
}


/* =========================================================
   STREAMLIT METRICS
   ========================================================= */

[data-testid="stMetricLabel"] {
    font-size: 19px !important;
}

[data-testid="stMetricValue"] {
    font-size: 34px !important;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] label {
    font-size: 17px !important;
}

[data-testid="stSidebar"] input {
    font-size: 18px !important;
}


/* =========================================================
   SUBHEADERS
   ========================================================= */

[data-testid="stSubheader"] {
    font-size: 30px !important;
    font-weight: 700 !important;
}


/* =========================================================
   ATTACK HISTORY TABLE
   ========================================================= */

.history-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    font-size: 18px;
}

.history-table th {
    background-color: #f1f5f9;
    color: #334155;
    font-size: 18px;
    font-weight: 700;
    padding: 16px 12px;
    text-align: left;
    border-bottom: 2px solid #cbd5e1;
}

.history-table td {
    font-size: 17px;
    padding: 15px 12px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
}

.history-table tr:hover {
    background-color: #f8fafc;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🛡️ AI-Based 5G Cyber Defense</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Real-Time 5G Security Monitoring & Autonomous Defense'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ============================================================
# LOAD SYSTEM INFORMATION
# ============================================================

api_status = False
database_status = False
logs_data = []


try:

    api_response = requests.get(
        "http://127.0.0.1:8000/",
        timeout=2
    )

    if api_response.status_code == 200:
        api_status = True

except Exception:
    api_status = False


try:

    logs_response = requests.get(
        "http://127.0.0.1:8000/logs",
        timeout=2
    )

    if logs_response.status_code == 200:

        database_status = True

        logs_data = logs_response.json().get(
            "logs",
            []
        )

except Exception:
    database_status = False


# ============================================================
# SYSTEM STATUS
# ============================================================

st.markdown(
    '<div class="section-title">🟢 System Status</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    if api_status:

        st.markdown("""
        <div class="status-card">
            <div class="status-title">FASTAPI SERVER</div>
            <div class="status-value">🟢 ONLINE</div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="status-card">
            <div class="status-title">FASTAPI SERVER</div>
            <div class="status-value">🔴 OFFLINE</div>
        </div>
        """, unsafe_allow_html=True)


with col2:

    if api_status:

        st.markdown("""
        <div class="status-card">
            <div class="status-title">AI MODEL</div>
            <div class="status-value">🟢 ACTIVE</div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="status-card">
            <div class="status-title">AI MODEL</div>
            <div class="status-value">🔴 OFFLINE</div>
        </div>
        """, unsafe_allow_html=True)


with col3:

    if database_status:

        st.markdown("""
        <div class="status-card">
            <div class="status-title">DATABASE</div>
            <div class="status-value">🟢 CONNECTED</div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="status-card">
            <div class="status-title">DATABASE</div>
            <div class="status-value">🔴 OFFLINE</div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# AI MODEL INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🤖 AI Model Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown("""
    <div class="model-card">
        <div class="model-label">CLASSIFICATION MODEL</div>
        <div class="model-value">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="model-card">
        <div class="model-label">TEST ACCURACY</div>
        <div class="model-value">81.25%</div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="model-card">
        <div class="model-label">KNOWN CLASSES</div>
        <div class="model-value">8</div>
    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="model-card">
        <div class="model-label">ANOMALY DETECTION</div>
        <div class="model-value">Isolation Forest</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CURRENT PROTECTION STATUS
# ============================================================

threats_detected = 0
sources_isolated = 0


for log in logs_data:

    # DATABASE ORDER:
    #
    # 0 = id
    # 1 = timestamp
    # 2 = prediction
    # 3 = confidence
    # 4 = threat_level
    # 5 = defense_action
    # 6 = source

    attack_type = log[2]
    defense_action = log[5]

    if attack_type != "normal":
        threats_detected += 1

    if defense_action:

        action_text = str(
            defense_action
        ).lower()

        if (
            "isolated" in action_text
            or "blocked" in action_text
        ):

            sources_isolated += 1


st.markdown(
    '<div class="section-title">🛡️ Current Protection Status</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("""
    <div class="protection-card">
        <div class="status-title">PROTECTION STATUS</div>
        <div class="protection-active">🟢 ACTIVE</div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="protection-card">
        <div class="status-title">THREATS DETECTED</div>
        <div class="protection-active">{threats_detected}</div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div class="protection-card">
        <div class="status-title">SOURCES ISOLATED</div>
        <div class="protection-active">{sources_isolated}</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")


# ============================================================
# NETWORK TRAFFIC INPUT
# ============================================================

st.sidebar.header("⚙️ Network Traffic Input")


packet_rate = st.sidebar.number_input(
    "Packet Rate",
    min_value=0,
    value=7000
)


packet_size = st.sidebar.number_input(
    "Packet Size",
    min_value=0,
    value=100
)


connection_count = st.sidebar.number_input(
    "Connection Count",
    min_value=0,
    value=1200
)


failed_connections = st.sidebar.number_input(
    "Failed Connections",
    min_value=0,
    value=900
)


traffic_duration = st.sidebar.number_input(
    "Traffic Duration",
    min_value=0,
    value=6
)


analyze = st.sidebar.button(
    "🔍 Analyze Traffic",
    use_container_width=True
)


# ============================================================
# DETECTION
# ============================================================

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
            json=data,
            timeout=5
        )

        result = response.json()


        st.markdown(
            '<div class="section-title">🎯 Detection Result</div>',
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
            '<div class="section-title">🛡️ Autonomous Defense</div>',
            unsafe_allow_html=True
        )


        st.info(
            result["defense_action"]
        )


        if result["severity"] == "Critical":

            st.error(
                "🚨 CRITICAL THREAT DETECTED"
            )

        elif result["severity"] == "High":

            st.warning(
                "⚠️ HIGH THREAT DETECTED"
            )

        elif result["severity"] == "Medium":

            st.warning(
                "⚠️ MEDIUM THREAT DETECTED"
            )

        else:

            st.success(
                "✅ NETWORK TRAFFIC IS NORMAL"
            )


    except Exception as e:

        st.error(
            "Unable to connect to the FastAPI server."
        )

        st.write(e)


# ============================================================
# SECURITY OVERVIEW
# ============================================================

st.markdown("---")


st.markdown(
    '<div class="section-title">📊 Security Overview</div>',
    unsafe_allow_html=True
)


if logs_data:

    total_events = len(logs_data)


    # ========================================================
    # CORRECT DATABASE INDEXES
    #
    # 0 = ID
    # 1 = Timestamp
    # 2 = Attack Type
    # 3 = Confidence
    # 4 = Severity
    # 5 = Defense Action
    # 6 = Source
    # ========================================================


    critical_count = sum(
        1
        for log in logs_data
        if log[4] == "Critical"
    )


    high_count = sum(
        1
        for log in logs_data
        if log[4] == "High"
    )


    medium_count = sum(
        1
        for log in logs_data
        if log[4] == "Medium"
    )


    attack_types = set(
        log[2]
        for log in logs_data
        if log[2] != "normal"
    )


    # ========================================================
    # SECURITY METRICS
    # ========================================================

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


    # ========================================================
    # ATTACK TYPE DISTRIBUTION
    # ========================================================

    st.subheader(
        "📈 Attack Type Distribution"
    )


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
            columns=[
                "Attack Type",
                "Count"
            ]
        )


        fig_attack = px.bar(
            chart_data,
            x="Attack Type",
            y="Count",
            text="Count"
        )


        fig_attack.update_traces(
            textfont_size=18
        )


        fig_attack.update_layout(
            height=480,
            xaxis=dict(
                title=dict(
                    text="Attack Type",
                    font=dict(size=20)
                ),
                tickfont=dict(size=17)
            ),
            yaxis=dict(
                title=dict(
                    text="Count",
                    font=dict(size=20)
                ),
                tickfont=dict(size=17)
            ),
            font=dict(size=17),
            margin=dict(
                l=70,
                r=30,
                t=30,
                b=100
            )
        )


        st.plotly_chart(
            fig_attack,
            use_container_width=True
        )


    else:

        st.info(
            "No attacks detected yet."
        )


    # ========================================================
    # SEVERITY DISTRIBUTION
    # ========================================================

    st.subheader(
        "🚨 Severity Distribution"
    )


    severity_counts = {
        "Critical": critical_count,
        "High": high_count,
        "Medium": medium_count
    }


    severity_data = pd.DataFrame(
        list(severity_counts.items()),
        columns=[
            "Severity",
            "Count"
        ]
    )


    fig_severity = px.bar(
        severity_data,
        x="Severity",
        y="Count",
        text="Count"
    )


    fig_severity.update_traces(
        textfont_size=18
    )


    fig_severity.update_layout(
        height=430,
        xaxis=dict(
            title=dict(
                text="Severity",
                font=dict(size=20)
            ),
            tickfont=dict(size=18)
        ),
        yaxis=dict(
            title=dict(
                text="Count",
                font=dict(size=20)
            ),
            tickfont=dict(size=17)
        ),
        font=dict(size=17),
        margin=dict(
            l=70,
            r=30,
            t=30,
            b=80
        )
    )


    st.plotly_chart(
        fig_severity,
        use_container_width=True
    )


    # ========================================================
    # ATTACK HISTORY
    # ========================================================

    st.markdown("---")


    st.subheader(
        "📋 Attack History"
    )


    history = []


    for log in logs_data:

        history.append({

            "ID": log[0],

            "Timestamp": log[1],

            "Attack Type": str(
                log[2]
            ).upper(),

            "Source": (
                log[6]
                if log[6]
                else "UE-Unknown"
            ),

            "Confidence": (
                f"{log[3]}%"
            ),

            "Severity": log[4],

            "Defense Action": log[5]

        })


    history_df = pd.DataFrame(
        history
    )


    # ========================================================
    # LARGE ATTACK HISTORY TABLE
    # ========================================================

    table_html = history_df.to_html(
        index=False,
        classes="history-table",
        escape=True
    )


    st.markdown(
        table_html,
        unsafe_allow_html=True
    )


else:

    st.info(
        "No security events recorded yet."
    )
