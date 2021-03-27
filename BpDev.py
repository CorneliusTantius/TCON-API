import os
from flask import jsonify, Blueprint,request
from Utils.DevController import getuid_dev, deletebyuid_dev

dev_bp = Blueprint('dev_bp',__name__)

@dev_bp.route("/dev/cleanup", methods = ["GET"])
def dev_cleanup():
    os.system("pyclean .")
    return jsonify(message = "pycache cleaned")

@dev_bp.route("/dev/getuid", methods = ["GET"])
def dev_getuid():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)
    return jsonify(message = getuid_dev(data))

@dev_bp.route("/dev/deletebyuid", methods = ["POST"])
def dev_deletebyuid():
    try:
        data = request.get_json(silent=True)
    except:
        return jsonify(message = "Failed to Fetch JSON Payload", status = False)
    return jsonify(message = deletebyuid_dev(data))