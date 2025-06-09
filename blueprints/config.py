from flask import request, jsonify, Blueprint, send_file
from dotenv import load_dotenv
import os, logging
from modules.cleaner import Cleaner
from modules.file_manager import File_Manager as fm
logger = logging.getLogger(__name__)


load_dotenv()
FileManager = fm()
Available_date = ['1h', '1d', '3d', '7d']
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data/temp')
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = os.getenv('MAX_SIZE') * 1024 * 1024
bp = Blueprint('config', __name__)


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "파일이 없습니다"}), 400
    file = request.files['file']
    date = request.form['date']
    if date not in Available_date:
        return jsonify({"error": "시간 설정 오류"}), 400
    if file.filename == '':
        return jsonify({"error": "선택된 파일이 없습니다"}), 400
    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return jsonify({"message": "업로드 성공", "filename": filename})
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    logger.info(f"업로드 성공 : {file.filename}")
    link = FileManager.save_file(file_path, date)
    return jsonify({"message": "업로드 성공", "link": link, "status": 0})

    # return jsonify({"error": "허용되지 않은 파일 형식"}), 400

@bp.route('/file/<link>', methods=['GET'])
def get_file(link):
    file_path = FileManager.get_file(link)
    if file_path:
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "파일을 찾을 수 없습니다"}), 404
