from logging.config import dictConfig

from flask import Flask

from .blueprint_service import api as blueprint_service
from .errors import errors
from .settings import LOGGERS

# Applies logger config to app instance
dictConfig(LOGGERS)
app = Flask(__name__)

# loading blueprints
app.register_blueprint(errors)
app.register_blueprint(blueprint_service, url_prefix="/api/v1")
