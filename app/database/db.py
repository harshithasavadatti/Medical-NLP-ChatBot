import sqlite3
from app.config import settings


DB_PATH = settings.SQL_DB_PATH


def get_connection():

    conn = sqlite3.connect(
        DB_PATH,
        check_same_thread=False   # ← important fix
    )

    conn.row_factory = sqlite3.Row

    return conn