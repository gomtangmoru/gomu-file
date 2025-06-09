import os, shutil
from uuid import uuid4
from datetime import datetime, timedelta
from .storage_db import Storage_DB

class File_Manager:
    def __init__(self):
        self.target_location = os.path.join(os.getcwd(), 'data/storage')
        temp_location = os.path.join(os.getcwd(), 'data/temps')
        self.storage_db = Storage_DB()

    def save_file(self, file_path: str, date: str):
        link = uuid4().hex[:8]
        original_filename = os.path.basename(file_path)
        rename_filename = f"{link}_{original_filename}"
        if date == "1h": expires_at = datetime.now() + timedelta(hours=1)
        elif date == "1d": expires_at = datetime.now() + timedelta(days=1)
        elif date == "3d": expires_at = datetime.now() + timedelta(days=3)
        elif date == "7d": expires_at = datetime.now() + timedelta(days=7)
        else: raise ValueError("Invalid date")
        shutil.move(file_path, os.path.join(self.target_location, rename_filename))
        self.storage_db.insert_file(link, original_filename, rename_filename, expires_at.isoformat())
        return link