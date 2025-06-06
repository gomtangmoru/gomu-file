from flask import request, Blueprint, jsonify

bp = Blueprint('upload', __name__)


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'saved/{file.filename}')
    return jsonify({'status':0})
    