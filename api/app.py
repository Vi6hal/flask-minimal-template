from flask import Flask, Response, jsonify, request

from .errors import errors

app = Flask(__name__)

app.register_blueprint(errors)


@app.route("/")
def index():
    return jsonify({"api_version":"v0.0.1"}), 200
