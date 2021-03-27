import os
from flask import Flask, request, jsonify
from Utils.AuthController import register_user, login_user

app = Flask(__name__)

@app.route("/dev/cleanup", methods = ["GET"])
def dev_cleanup():
    os.system("pyclean .")
    return jsonify(message = "pycache cleaned")

@app.route("/auth/login", methods = ["GET"])
def auth_login():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload")
    ret = login_user(data)
    if(ret == "Done"):
        del ret, data
        return jsonify(message = True)
    else:
        del data
        return jsonify(message = ret)

@app.route("/auth/register", methods = ["POST"])
def auth_register():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload")
    ret = register_user(data)
    if(ret == 'Done'):
        del ret, data
        return jsonify(message = "Register Success")
    else:
        del data
        return jsonify(message = ret)

if __name__ == '__main__':
    app.run(host='localhost',threaded=True)
    os.system("pyclean .")