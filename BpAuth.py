import os
from flask import request, jsonify, Blueprint
from Utils.AuthController import register_user, login_user
from Utils.ConsultantController import register_consultant

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route("/auth/login", methods = ["GET"])
def auth_login():
    try:
        data = request.get_json(silent=True)
        ret, isConsultant, uid, stat = login_user(data)
        return jsonify(message = ret, status = stat, userId = uid, isConsultant=isConsultant)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status=False, userId = "", isConsultant = 0)

@auth_bp.route("/auth/register", methods = ["POST"])
def auth_register():
    try:
        data = request.get_json(silent=True)
        ret, stat = register_user(data)
        return jsonify(message = ret, status = stat)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)

