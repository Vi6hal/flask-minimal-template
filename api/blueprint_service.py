from flask import Blueprint, current_app, jsonify

api = Blueprint("privilege", __name__)


@api.route("/")
def get_data():
    current_app.logger.info("main debug")
    return (jsonify({"api_version": "v1.0.0", "about": "A BLueprint Example"}), 200)
