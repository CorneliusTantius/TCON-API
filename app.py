import os
from flask import Flask
from BpAuth import auth_bp
from BpConsultant import consultant_bp
from BpDev import dev_bp
from BpUser import user_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(consultant_bp)
app.register_blueprint(dev_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    return "<h1>TCon-API V1.2</h1>"

if __name__ == "__main__":
    os.system("pyclean .")
    app.run(threaded=True, port=5000)
    os.system("pyclean .")