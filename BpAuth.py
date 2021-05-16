import os
from flask import request, jsonify, Blueprint
from Utils.AuthController import register_user, login_user
from Utils.ConsultantController import register_consultant

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route("/auth/login", methods = ["GET"])
def auth_login():
    try:
        data = request.get_json(silent=True)
    except:
        retval = jsonify(message = "Failed to Fetch JSON Payload", status=False)
        retval.headers.add('Access-Control-Allow-Origin', '*')
        return retval
    ret, isConsultant, uid = login_user(data)
    if(ret == "Done"):
        del ret, data
        retval = jsonify(message = "User Logged In", status = True, userId = uid, isConsultant=isConsultant)
        retval.headers.add('Access-Control-Allow-Origin', '*')
        return retval
    else:
        del data
        retval = jsonify(message = ret, status = False, userId = uid, isConsultant=isConsultant)
        retval.headers.add('Access-Control-Allow-Origin', '*')
        return retval

@auth_bp.route("/auth/register", methods = ["POST"])
def auth_register():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)
    try:
        ret = register_user(data)
    except:
        return jsonify(message = "Register Failed, Try Again", status = False)
    if(ret == 'Done'):
        del ret, data
        return jsonify(message = "Register Success", status = True)
    else:
        del data
        return jsonify(message = ret, status =False)

