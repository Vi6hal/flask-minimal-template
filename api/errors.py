from flask import Blueprint,Response
from flask import json
from werkzeug.exceptions import HTTPException
import sys, traceback

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@errors.app_errorhandler(ValueError)
def handle_exception_value(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = Response()
    response.data = json.dumps({
        "name": str(e.__repr__()),
        "traceback": ''.join(traceback.format_tb(e.__traceback__))
        })
    response.status_code = 400
    response.content_type = "application/json"
    return response
