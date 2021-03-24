import os
from flask import Flask, request, jsonify
from Utils.AuthController import register_user, login_user

app = Flask(__name__)

@app.route("/auth/login", methods = ["GET"])
def auth_login():
    data = request.get_json(silent=True)
    ret = login_user(data)
    if(ret == "Done"):
        del ret, data
        return jsonify(res = True)
    else:
        del data
        return jsonify(res = ret)

@app.route("/auth/register", methods = ["POST"])
def auth_register():
    data = request.get_json(silent=True)
    ret = register_user(data)
    if(ret == 'Done'):
        del ret, data
        return jsonify(res = "register success")
    else:
        del data
        return jsonify(res = ret)

if __name__ == '__main__':
	app.run(host='localhost',threaded=True)