import os
import uuid

def save_file(file, upload_folder):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    ext = os.path.splitext(file.filename)[-1]
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    return file_path
