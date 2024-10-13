from flask import render_template
from . import auth_bp

@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('auth/index.html')