import os
from flask import request, jsonify, Blueprint, Response
from Controller.AuthController import register_user, login_user
from Controller.ConsultantController import register_consultant
from flask_cors import cross_origin

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route("/auth/login", methods = ["POST"])
@cross_origin()
def auth_login():
    try:
        data = request.get_json(silent=True)
        ret, res, stat = login_user(data)        
        return jsonify(message = ret, status = stat, 
            userId =  res[2], name = str(res[3] +" "+ res[4]), email = res[5], phone = res[6], isConsultant=res[1])
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status=False, userId = "", name="", email="", phone="", isConsultant = 0)

@auth_bp.route("/auth/register", methods = ["POST"])
@cross_origin()
def auth_register():
    try:
        data = request.get_json(silent=True)
        ret, stat = register_user(data)
        return jsonify(message = ret, status = stat)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)

