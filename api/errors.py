import traceback

from flask import Blueprint, Response, json
from werkzeug.exceptions import HTTPException

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""

    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@errors.app_errorhandler(ValueError)
def handle_exception_value(e):
    """Return JSON instead of HTML for Python errors."""
    response = Response()
    response.data = json.dumps(
        {
            "name": str(e.__repr__()),
            "traceback": "".join(traceback.format_tb(e.__traceback__)),
        }
    )
    response.status_code = 400
    response.content_type = "application/json"
    return response
