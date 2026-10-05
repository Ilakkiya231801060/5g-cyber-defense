import sqlite3
from datetime import datetime

DB_NAME = "data/cyber_defense.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attack_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prediction TEXT,
            source TEXT,
            confidence REAL,
            threat_level TEXT,
            defense_action TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_attack(
    prediction,
    source,
    confidence,
    threat_level,
    defense_action
):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO attack_logs
        (timestamp, prediction, source, confidence, threat_level, defense_action)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        prediction,
        source,
        confidence,
        threat_level,
        defense_action
    ))

    conn.commit()
    conn.close()


def get_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM attack_logs
        ORDER BY id DESC
    """)

    logs = cursor.fetchall()

    conn.close()

    return logs


create_database()
