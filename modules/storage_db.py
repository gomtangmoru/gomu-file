import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("data/storage.db")
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

def insert_file(file_id, original_filename, filepath, expires_at):
    conn = sqlite3.connect("data/storage.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO files (file_id, original_filename, filepath, uploaded_at, expires_at)
        VALUES (?, ?, ?, ?, ?)
    """, (file_id, original_filename, filepath, datetime.now().isoformat(), expires_at.isoformat()))
    conn.commit()
    conn.close()

def get_file(file_id):
    conn = sqlite3.connect("data/storage.db")
    cur = conn.cursor()
    cur.execute("SELECT original_filename, filepath, expires_at FROM files WHERE file_id = ?", (file_id,))
    result = cur.fetchone()
    conn.close()
    return result

def delete_file(file_id):
    conn = sqlite3.connect("data/storage.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM files WHERE file_id = ?", (file_id,))
    conn.commit()
    conn.close()
