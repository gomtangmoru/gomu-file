from flask import request, Blueprint, jsonify
from dotenv import load_dotenv
import os, logging

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