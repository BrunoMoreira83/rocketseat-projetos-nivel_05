from flask import Blueprint, jsonify

pets_route_bp = Blueprint("pets", __name__)

@pets_route_bp.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"Ola": "Mundo"}), 200
