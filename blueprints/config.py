import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data/uploads')
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

from flask import request, jsonify, Blueprint
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import config

load_dotenv()
MAX_CONTENT_LENGTH = os.getenv('MAX_SIZE') * 1024 * 1024
# app = Flask(__name__)
bp = Blueprint('config', __name__)

bp.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
bp.config['MAX_CONTENT_LENGTH'] = config.MAX_CONTENT_LENGTH

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "파일이 없습니다"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "선택된 파일이 없습니다"}), 400
    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return jsonify({"message": "업로드 성공", "filename": filename})
    return jsonify({"message": "업로드 성공", "filename": file.filename})

    # return jsonify({"error": "허용되지 않은 파일 형식"}), 400

# NOT FOR USE

# @bp.route('/files', methods=['GET'])
# def list_files():
#     files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return jsonify({"files": files})

