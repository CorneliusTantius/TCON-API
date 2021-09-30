import os
from flask import request, jsonify, Blueprint
from Utils.UserController import *
from flask_cors import cross_origin

user_bp = Blueprint('user_bp',__name__)

@user_bp.route("/user/newchat", methods = ["POST"])
@cross_origin()
def user_newchat():
    try:
        data = request.get_json(silent=True)
        ret,status = create_new_chat(data)
        return jsonify(result = ret, status = status)
    except:
        return jsonify(result = "Failed to Fetch JSON Payload", status=False)

@user_bp.route("/user/getchatheader", methods = ["POST"])
@cross_origin()
def user_getchatheader():
    try:
        data = request.get_json(silent=True)
        ret, status = get_all_chat_header(data)
        return jsonify(result = ret, status = status)
    except:
        return jsonify(result = "Failed to Fetch JSON Payload", status = False)


@user_bp.route("/user/sendchat", methods = ["POST"])
@cross_origin()
def user_sendchat():
    try:
        data = request.get_json(silent=True)
        ret, status = sendchat(data)
        return jsonify(result = ret, status = status)
    except:
        return jsonify(result = "Failed to Fetch JSON Payload", status = False)

@user_bp.route("/user/getchatdetails", methods = ["POST"])
@cross_origin()
def user_getchatdetails():
    try:
        data = request.get_json(silent=True)
        ret, status = getchatdetails(data)
        return jsonify(result = ret, status = status)
    except:
        return jsonify(result = "Failed to Fetch JSON Payload", status = False)