import sqlite3
from datetime import datetime


class Storage_DB:
    def __init__(self):
        self.conn = sqlite3.connect("data/storage.db")
        self.init_db()

    def init_db(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS files (
                file_id TEXT PRIMARY KEY,
                original_filename TEXT,
                filepath TEXT,
                uploaded_at TEXT,
                expires_at TEXT
            )
        """)
        self.conn.commit()
        self.conn.close()

    def insert_file(self, file_id, original_filename, filepath, expires_at):
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO files (file_id, original_filename, filepath, uploaded_at, expires_at)
            VALUES (?, ?, ?, ?, ?)
        """, (file_id, original_filename, filepath, datetime.now().isoformat(), expires_at.isoformat()))
        self.conn.commit()
        self.conn.close()

    def get_file(self, file_id):
        cur = self.conn.cursor()
        cur.execute("SELECT original_filename, filepath, expires_at FROM files WHERE file_id = ?", (file_id,))
        result = cur.fetchone()
        self.conn.close()
        return result

    def delete_file(self, file_id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM files WHERE file_id = ?", (file_id,))
        self.conn.commit()
        self.conn.close()
