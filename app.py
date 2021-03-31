from flask import Flask
from BpAuth import auth_bp
from BpConsultant import consultant_bp
from BpDev import dev_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(consultant_bp)
app.register_blueprint(dev_bp)

@app.route('/')
def index():
    return "<h1>TCon-API</h1>"