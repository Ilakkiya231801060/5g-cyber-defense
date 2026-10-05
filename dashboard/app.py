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
# PROFESSIONAL DARK THEME
# ============================================================

st.markdown("""
<style>

/* =========================================================
   MAIN APPLICATION
   ========================================================= */

.stApp {
    background-color: #080c12 !important;
    color: #f1f5f9 !important;
}

.main {
    background-color: #080c12 !important;
}

.block-container {
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
}


/* =========================================================
   GENERAL TEXT
   ========================================================= */

body,
p,
span,
label,
div {
    font-family:
        "Inter",
        "Segoe UI",
        Arial,
        sans-serif;
}


/* =========================================================
   MAIN HEADER
   ========================================================= */

.main-title {
    font-size: 38px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}

.subtitle {
    font-size: 17px;
    font-weight: 400;
    color: #94a3b8;
    margin-bottom: 24px;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    font-size: 27px;
    font-weight: 700;
    color: #f8fafc;
    margin-top: 28px;
    margin-bottom: 18px;
}


/* =========================================================
   STATUS CARDS
   ========================================================= */

.status-card {
    padding: 20px;
    min-height: 108px;
    border-radius: 12px;
    background-color: #0f1620;
    border: 1px solid #263241;
    text-align: center;
    margin-bottom: 16px;
}

.status-title {
    font-size: 14px;
    font-weight: 600;
    color: #94a3b8;
    margin-bottom: 9px;
    letter-spacing: 0.3px;
}

.status-value {
    font-size: 22px;
    font-weight: 700;
    color: #f8fafc;
}


/* =========================================================
   MODEL CARDS
   ========================================================= */

.model-card {
    padding: 20px;
    min-height: 115px;
    border-radius: 12px;
    background-color: #0f1620;
    border: 1px solid #263241;
}

.model-label {
    font-size: 14px;
    font-weight: 600;
    color: #94a3b8;
    letter-spacing: 0.2px;
}

.model-value {
    font-size: 21px;
    font-weight: 700;
    color: #f8fafc;
    margin-top: 10px;
}


/* =========================================================
   PROTECTION CARDS
   ========================================================= */

.protection-card {
    padding: 20px;
    min-height: 105px;
    border-radius: 12px;
    background-color: #0f1620;
    border: 1px solid #263241;
    text-align: center;
}

.protection-active {
    font-size: 22px;
    font-weight: 700;
    color: #f8fafc;
}


/* =========================================================
   STREAMLIT METRICS
   ========================================================= */

[data-testid="stMetric"] {
    background-color: #0f1620 !important;
    border: 1px solid #263241 !important;
    border-radius: 12px !important;
    padding: 18px !important;
}

[data-testid="stMetricLabel"] {
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #cbd5e1 !important;
}

[data-testid="stMetricValue"] {
    font-size: 29px !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
}

[data-testid="stMetricDelta"] {
    font-size: 14px !important;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {
    background-color: #090e15 !important;
    border-right: 1px solid #263241 !important;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] label {
    color: #cbd5e1 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

[data-testid="stSidebar"] input {
    background-color: #ffffff !important;
    color: #111827 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}


/* Number input buttons */

[data-testid="stSidebar"] button {
    color: #cbd5e1 !important;
}


/* =========================================================
   SIDEBAR ANALYZE BUTTON
   ========================================================= */

[data-testid="stSidebar"] .stButton button {
    background-color: #111827 !important;
    color: #e2e8f0 !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    min-height: 42px !important;
}

[data-testid="stSidebar"] .stButton button:hover {
    border-color: #64748b !important;
    color: #ffffff !important;
}


/* =========================================================
   SUBHEADERS
   ========================================================= */

[data-testid="stSubheader"] {
    font-size: 22px !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
    margin-top: 24px !important;
    margin-bottom: 14px !important;
}


/* =========================================================
   NORMAL STREAMLIT TEXT
   ========================================================= */

.stMarkdown {
    color: #e2e8f0;
}


/* =========================================================
   ALERT BOXES
   ========================================================= */

[data-testid="stAlert"] {
    border-radius: 10px !important;
}


/* =========================================================
   ATTACK HISTORY TABLE
   ========================================================= */

.history-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    background-color: #0f1620;
    border: 1px solid #263241;
    border-radius: 10px;
    overflow: hidden;
    font-size: 14px;
}

.history-table th {
    background-color: #151e2b;
    color: #e2e8f0;
    font-size: 14px;
    font-weight: 700;
    padding: 13px 11px;
    text-align: left;
    border-bottom: 1px solid #334155;
}

.history-table td {
    font-size: 14px;
    padding: 12px 11px;
    border-bottom: 1px solid #1e293b;
    color: #cbd5e1;
}

.history-table tr:hover {
    background-color: #141e2a;
}


/* =========================================================
   HORIZONTAL LINE
   ========================================================= */

hr {
    border: none !important;
    border-top: 1px solid #263241 !important;
    margin: 24px 0 !important;
}


/* =========================================================
   CHART CONTAINER
   ========================================================= */

.chart-container {
    background-color: #0f1620;
    border: 1px solid #263241;
    border-radius: 12px;
    padding: 10px;
}


/* =========================================================
   REMOVE EXTRA TOP WHITE AREA
   ========================================================= */

header[data-testid="stHeader"] {
    background-color: #080c12 !important;
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
# INITIAL SYSTEM VARIABLES
# ============================================================

api_status = False
database_status = False
logs_data = []


# ============================================================
# CHECK FASTAPI SERVER
# ============================================================

try:

    api_response = requests.get(
        "http://127.0.0.1:8000/",
        timeout=2
    )

    if api_response.status_code == 200:
        api_status = True

except Exception:
    api_status = False


# ============================================================
# LOAD DATABASE LOGS
# ============================================================

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
# HELPER FUNCTION
# SUPPORTS BOTH POSSIBLE DATABASE COLUMN ORDERS
# ============================================================

def parse_log(log):

    """
    Supports:

    New schema:
    0 = id
    1 = timestamp
    2 = prediction
    3 = source
    4 = confidence
    5 = threat_level
    6 = defense_action

    Old schema:
    0 = id
    1 = timestamp
    2 = prediction
    3 = confidence
    4 = threat_level
    5 = defense_action
    6 = source
    """

    attack_type = log[2]

    if isinstance(log[3], (int, float)):

        # OLD DATABASE ORDER

        source = (
            log[6]
            if len(log) > 6 and log[6]
            else "UE-Unknown"
        )

        confidence = log[3]

        severity = (
            log[4]
            if len(log) > 4
            else "Unknown"
        )

        defense_action = (
            log[5]
            if len(log) > 5
            else ""
        )

    else:

        # NEW DATABASE ORDER

        source = (
            log[3]
            if len(log) > 3 and log[3]
            else "UE-Unknown"
        )

        confidence = (
            log[4]
            if len(log) > 4
            else 0
        )

        severity = (
            log[5]
            if len(log) > 5
            else "Unknown"
        )

        defense_action = (
            log[6]
            if len(log) > 6
            else ""
        )

    return {
        "id": log[0],
        "timestamp": log[1],
        "attack_type": attack_type,
        "source": source,
        "confidence": confidence,
        "severity": severity,
        "defense_action": defense_action
    }


# ============================================================
# CONVERT DATABASE LOGS
# ============================================================

parsed_logs = []

for log in logs_data:

    try:

        parsed_logs.append(
            parse_log(log)
        )

    except Exception:
        pass


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


for log in parsed_logs:

    attack_type = str(
        log["attack_type"]
    ).lower()

    defense_action = str(
        log["defense_action"]
    ).lower()

    if attack_type != "normal":

        threats_detected += 1

    if (
        "isolated" in defense_action
        or "blocked" in defense_action
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


        # ====================================================
        # IMPORTANT:
        # RELOAD LOGS AFTER NEW ANALYSIS
        # ====================================================

        try:

            updated_logs_response = requests.get(
                "http://127.0.0.1:8000/logs",
                timeout=2
            )

            if updated_logs_response.status_code == 200:

                logs_data = (
                    updated_logs_response
                    .json()
                    .get("logs", [])
                )

                parsed_logs = []

                for log in logs_data:

                    try:

                        parsed_logs.append(
                            parse_log(log)
                        )

                    except Exception:
                        pass

        except Exception:

            pass


        # ====================================================
        # DETECTION RESULT
        # ====================================================

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


        # ====================================================
        # AUTONOMOUS DEFENSE
        # ====================================================

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

        elif result["severity"] == "Low":

            st.info(
                "ℹ️ LOW THREAT DETECTED"
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


if parsed_logs:

    total_events = len(
        parsed_logs
    )


    # ========================================================
    # COUNT SEVERITIES
    # ========================================================

    critical_count = sum(
        1
        for log in parsed_logs
        if str(log["severity"]).lower() == "critical"
    )


    high_count = sum(
        1
        for log in parsed_logs
        if str(log["severity"]).lower() == "high"
    )


    medium_count = sum(
        1
        for log in parsed_logs
        if str(log["severity"]).lower() == "medium"
    )


    low_count = sum(
        1
        for log in parsed_logs
        if str(log["severity"]).lower() == "low"
    )


    # ========================================================
    # ATTACK TYPES
    # ========================================================

    attack_types = set()

    for log in parsed_logs:

        attack = str(
            log["attack_type"]
        ).lower()

        if attack != "normal":

            attack_types.add(
                attack
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


    for log in parsed_logs:

        attack = str(
            log["attack_type"]
        ).lower()

        if attack != "normal":

            attack_counts[attack] = (
                attack_counts.get(
                    attack,
                    0
                ) + 1
            )


    if attack_counts:

        chart_data = pd.DataFrame(
            list(
                attack_counts.items()
            ),
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
            textfont_size=14,
            textposition="outside"
        )


        fig_attack.update_layout(
            height=430,
            template="plotly_dark",
            paper_bgcolor="#0f1620",
            plot_bgcolor="#0f1620",
            font=dict(
                family="Inter, Segoe UI, Arial",
                size=14,
                color="#e2e8f0"
            ),
            xaxis=dict(
                title=dict(
                    text="Attack Type",
                    font=dict(
                        size=16,
                        color="#cbd5e1"
                    )
                ),
                tickfont=dict(
                    size=13,
                    color="#cbd5e1"
                ),
                gridcolor="#263241"
            ),
            yaxis=dict(
                title=dict(
                    text="Count",
                    font=dict(
                        size=16,
                        color="#cbd5e1"
                    )
                ),
                tickfont=dict(
                    size=13,
                    color="#cbd5e1"
                ),
                gridcolor="#263241"
            ),
            margin=dict(
                l=60,
                r=30,
                t=30,
                b=80
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

        "Critical":
            critical_count,

        "High":
            high_count,

        "Medium":
            medium_count,

        "Low":
            low_count

    }


    severity_data = pd.DataFrame(
        list(
            severity_counts.items()
        ),
        columns=[
            "Severity",
            "Count"
        ]
    )


    # ========================================================
    # ALWAYS SHOW THE SEVERITY CATEGORIES
    # ========================================================

    fig_severity = px.bar(
        severity_data,
        x="Severity",
        y="Count",
        text="Count"
    )


    fig_severity.update_traces(
        textfont_size=14,
        textposition="outside"
    )


    fig_severity.update_layout(
        height=430,
        template="plotly_dark",
        paper_bgcolor="#0f1620",
        plot_bgcolor="#0f1620",
        font=dict(
            family="Inter, Segoe UI, Arial",
            size=14,
            color="#e2e8f0"
        ),
        xaxis=dict(
            title=dict(
                text="Severity",
                font=dict(
                    size=16,
                    color="#cbd5e1"
                )
            ),
            tickfont=dict(
                size=14,
                color="#cbd5e1"
            ),
            gridcolor="#263241"
        ),
        yaxis=dict(
            title=dict(
                text="Count",
                font=dict(
                    size=16,
                    color="#cbd5e1"
                )
            ),
            tickfont=dict(
                size=13,
                color="#cbd5e1"
            ),
            gridcolor="#263241",
            rangemode="tozero"
        ),
        margin=dict(
            l=60,
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


    for log in parsed_logs:

        history.append({

            "ID":
                log["id"],

            "Timestamp":
                log["timestamp"],

            "Attack Type":
                str(
                    log["attack_type"]
                ).upper(),

            "Source":
                log["source"]
                if log["source"]
                else "UE-Unknown",

            "Confidence":
                f'{log["confidence"]}%',

            "Severity":
                log["severity"],

            "Defense Action":
                log["defense_action"]

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
