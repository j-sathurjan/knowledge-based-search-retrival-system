from flask import Blueprint, render_template

upload = Blueprint('upload',__name__, template_folder='templates', static_folder='static',url_prefix='/upload')

@upload.route('/')
def index():
    return render_template('doc_upload/index.html')