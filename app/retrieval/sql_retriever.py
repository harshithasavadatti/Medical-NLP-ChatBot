from app.database.db import get_connection


class SQLRetriever:

    def __init__(self):
        self.conn = get_connection()

    def validate_mrd(self, mrd_number):
        """
        Check if MRD exists
        """

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) as count FROM documents WHERE mrd_number = ?",
            (mrd_number,)
        )

        result = cursor.fetchone()

        return result["count"] > 0

    def get_patient_documents(self, mrd_number):
        """
        Retrieve all documents for a patient
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                mrd_number,
                visit_id,
                document_type,
                doctor_name,
                doctor_speciality,
                visit_type,
                adm_date,
                dschg_date
            FROM documents
            WHERE mrd_number = ?
            """,
            (mrd_number,)
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    def get_documents_by_type(self, mrd_number, doc_type):
        """
        Retrieve specific document types
        Example: discharge summary
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM documents
            WHERE mrd_number = ?
            AND document_type LIKE ?
            """,
            (mrd_number, f"%{doc_type}%")
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]