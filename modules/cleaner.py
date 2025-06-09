import os
import sqlite3, logging, threading
from time import sleep
from datetime import datetime
from modules.storage_db import Storage_DB

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
storage_db = Storage_DB()

class Cleaner:
    def __init__(self):
        self.conn = sqlite3.connect("data/storage.db")
        self.target_path = os.path.join(os.getcwd(), "data/storage")
        self.temp_path = os.path.join(os.getcwd(), "data/temps")
        
        
    def clean_folder(folder_path):
        """폴더 내 모든 파일 삭제"""
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    storage_db.delete_file(file_path)  # 파일 정보 DB에서도 제거 (옵션)
            except Exception as e:
                logging.error(f"파일 삭제 실패: {file_path} - {e}")


class Auto_cleaner:
    def __init__(self):
        self.running = True
        self.db_path = "data/storage.db"
        self.thread = threading.Thread(target=self.clean_expired_files)
        self.thread.daemon = True 
        self.target_path = os.path.join(os.getcwd(), "data/storage")
        self.temp_path = os.path.join(os.getcwd(), "data/temps")
    
    def start(self):
        self.thread.start()
        logging.info("Auto_cleaner 스레드 시작")

    def stop(self):
        self.running = False
        self.thread.join()
        logging.info("Auto_cleaner 스레드 종료")

    def clean_expired_files(self, interval_minutes=5):
        while self.running:
            try:
                expired_files = storage_db.get_expired_files()
                for file_id, filepath in expired_files:
                    filepath = os.path.join(self.target_path, filepath)
                    try:
                        if os.path.exists(filepath):
                            os.remove(filepath)
                            logging.info(f"[삭제됨] {file_id}")
                        storage_db.delete_file(file_id)
                    except Exception as e:
                        logging.error(f"[오류] {file_id} 삭제 실패: {e}")
            
            except Exception as e:
                logging.error(f"클리너 작업 중 오류 발생: {e}")
                
            sleep(interval_minutes * 60)

