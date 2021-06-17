import os
from flask import request, jsonify, Blueprint
from Utils.AuthController import register_user, login_user
from Utils.ConsultantController import register_consultant
from flask_cors import cross_origin

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route("/auth/login", methods = ["GET"])
@cross_origin()
def auth_login():
    try:
        data = request.get_json(silent=True)
        ret, isConsultant, uid, stat = login_user(data)
        return jsonify(message = ret, status = stat, userId = uid, isConsultant=isConsultant)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status=False, userId = "", isConsultant = 0)

@auth_bp.route("/auth/register", methods = ["POST"])
@cross_origin()
def auth_register():
    try:
        data = request.get_json(silent=True)
        ret, stat = register_user(data)
        return jsonify(message = ret, status = stat)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)

