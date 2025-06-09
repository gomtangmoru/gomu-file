from flask import Blueprint, render_template, session, redirect, url_for


bp = Blueprint('index', __name__, 
               template_folder='templates',
               static_folder='static',
               static_url_path='/static')

@bp.route('/')
def index():
    return render_template('index.html')

