from flask import Flask, render_template
from apps.auth.routes import auth_bp
from apps.doc_upload.routes import upload_bp
from database import db

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)