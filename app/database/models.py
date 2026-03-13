from app.database.db import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mrd_number TEXT,
        patient_id TEXT,
        visit_id TEXT,
        visit_type TEXT,
        document_type TEXT,
        doctor_name TEXT,
        doctor_speciality TEXT,
        adm_date TEXT,
        dschg_date TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_document(record):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO documents (
        mrd_number,
        patient_id,
        visit_id,
        visit_type,
        document_type,
        doctor_name,
        doctor_speciality,
        adm_date,
        dschg_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        record.get("mrd_number"),
        record.get("patient_id"),
        record.get("visit_id"),
        record.get("visit_type"),
        record.get("document_type"),
        record.get("doctor_name"),
        record.get("doctor_speciality"),
        record.get("adm_date"),
        record.get("dschg_date")
    ))

    conn.commit()
    conn.close()