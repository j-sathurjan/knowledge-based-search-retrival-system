from flask import Flask, render_template
from apps.auth.routes import auth
from apps.doc_upload.routes import upload

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(upload)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)