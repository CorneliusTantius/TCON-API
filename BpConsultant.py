import os
from flask import request, jsonify, Blueprint
from Controller.ConsultantController import register_consultant, getall_consultant, get_consultant_details
from flask_cors import cross_origin

consultant_bp = Blueprint('consultant_bp',__name__)

@consultant_bp.route("/consultant/register", methods = ["POST"])
@cross_origin()
def consultant_register():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)
    ret = register_consultant(data)
    if ret =='Done':
        return jsonify(message = "Registered New Consultant", status = True)
    else:
        return jsonify(message = ret, status = False)

@consultant_bp.route("/consultant/getall", methods = ["GET"])
@cross_origin()
def consultant_getall():
    return jsonify(consultants = getall_consultant())

@consultant_bp.route("/consultant/details", methods = ["POST"])
@cross_origin()
def consultant_getdetails():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)
    return jsonify(details = get_consultant_details(data))
