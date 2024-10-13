from flask import Blueprint

upload_bp = Blueprint('upload_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/upload')