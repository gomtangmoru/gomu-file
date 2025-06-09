from flask import Blueprint, render_template, session, redirect, url_for
import logging
from datetime import datetime

bp = Blueprint('index', __name__, 
               template_folder='templates',
               static_folder='static',
               static_url_path='/static')

@bp.route('/')
def index():
    return render_template('index.html')
  
# 로거 설정
  logger = logging.getLogger(__name__)
    #접속 로그 기록
    logger.info("Main page accessed")
  
    # 로그인 인증 체크 (선택적 적용)
    if 'user_id' not in session:
        logger.warning("비로그인 사용자 접근")
        return redirect(url_for('auth.login'))
    # 템플릿에 현재 시간 전달
    current_time = datetime.now()

    # 템플릿 렌더링
    return render_template('index.html', current_time=current_time)
