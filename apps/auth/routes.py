from flask import Blueprint, render_template

auth = Blueprint('auth',__name__,template_folder='templates',static_folder='static',url_prefix='/auth')

@auth.route('/', methods=['GET', 'POST'])
def index():
    return render_template('auth/index.html')