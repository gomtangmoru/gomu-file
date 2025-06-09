from flask import request, Blueprint, jsonify
from dotenv import load_dotenv
import os, logging
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)
load_dotenv()

MAX_SIZE = os.getenv('MAX_SIZE')

bp = Blueprint('upload', __name__)


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    date = request.form['date']
    available_date = ['1h', '1d', '3d', '7d']
    if date not in available_date:
        return jsonify({'status':1, 'message':'시간 설정 오류'})
    logger.debug(date)
    file.save(f'saved/{file.filename}')
    return jsonify({'status':0})


@bp.route('/max-size', methods=['GET'])
def max_size():
    return jsonify({'status':0, 'max_size':MAX_SIZE})

original_filename = file.filename ##여러파일 업로드 충돌 예방 중복방지 UUID 혹은 타임스탬프
ext = original_filename.rsplit('.', 1)[-1]  # 확장자 추출
unique_id = uuid.uuid4().hex  # 고유 UUID 생성
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')  # 타임스탬프

new_filename = f"{timestamp}_{unique_id}.{ext}"
file.save(f'saved/{new_filename}')
