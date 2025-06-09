import os
import sqlite3
from time import sleep
from datetime import datetime
from modules.storage_db import delete_file

def clean_folder(folder_path):
    """폴더 내 모든 파일 삭제"""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                delete_file(file_path)  # 파일 정보 DB에서도 제거 (옵션)
        except Exception as e:
            print(f"파일 삭제 실패: {file_path} - {e}")

def clean_expired_files(interval_minutes=5):
    while True:
        conn = sqlite3.connect("data/storage.db")
        cur = conn.cursor()
        cur.execute("SELECT file_id, filepath, expires_at FROM files")
        rows = cur.fetchall()
        now = datetime.now()

        for file_id, filepath, expires_at in rows:
            try:
                if now > datetime.fromisoformat(expires_at):
                    if os.path.exists(filepath):
                        os.remove(filepath)
                        print(f"[삭제됨] {file_id}")
                    delete_file(file_id)
            except Exception as e:
                print(f"[오류] {file_id} 삭제 실패: {e}")

        conn.close()
        sleep(interval_minutes * 60)

