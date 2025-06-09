import sqlite3
from datetime import datetime


class Storage_DB:
    def __init__(self):
        self.db_path = "data/storage.db"
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS files (
                file_id TEXT PRIMARY KEY,
                original_filename TEXT,
                filepath TEXT,
                uploaded_at TEXT,
                expires_at TEXT
            )
        """)
        conn.commit()
        conn.close()

    def insert_file(self, file_id : str, original_filename : str, filepath : str, expires_at : datetime):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO files (file_id, original_filename, filepath, uploaded_at, expires_at)
            VALUES (?, ?, ?, ?, ?)
        """, (file_id, original_filename, filepath, datetime.now().isoformat(), expires_at.isoformat() if isinstance(expires_at, datetime) else expires_at))
        conn.commit()
        conn.close()

    def get_file(self, file_id : str):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT original_filename FROM files WHERE file_id = ?", (file_id,))
        result = cur.fetchone()
        conn.close()
        return result[0] if result else None
    
    def get_file_path(self, file_id : str):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT filepath FROM files WHERE file_id = ?", (file_id,))
        result = cur.fetchone()
        conn.close()
        return result[0] if result else None

    def delete_file(self, file_id : str):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM files WHERE file_id = ?", (file_id,))
        conn.commit()
        conn.close()

    def get_expired_files(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT file_id, filepath FROM files WHERE expires_at < ?", (datetime.now().isoformat(),))
        result = cur.fetchall()
        conn.close()
        return result
