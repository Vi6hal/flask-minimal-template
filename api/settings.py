from pathlib import Path

DEBUG = True
BASE_PATH = Path(__file__).parent.parent.absolute()
LOG_PATH = BASE_PATH / "logs"

LOGGERS = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s %(module)s: %(message)s",
        },
        "debug": {
            "format": "[%(levelname)s][%(asctime)s][%(module)s] - %(name)s - : %(message)s %(pathname)s:%(lineno)d",
        },
        "access": {
            "format": "%(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": LOG_PATH / "gunicorn.error.log",
            "maxBytes": 10000,
            "backupCount": 10,
            "delay": "True",
        },
        "info": {
            "formatter": "default",
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH / "info.log",
            "mode": "a",
            "maxBytes": 1048576,
            "backupCount": 10,
        },
        "debug_log": {
            "formatter": "debug",
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH / "debug_info.log",
            "mode": "a",
            "maxBytes": 1048576,
            "backupCount": 10,
        },
        "access_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "access",
            "filename": LOG_PATH / "gunicorn.access.log",
            "maxBytes": 10000,
            "backupCount": 10,
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "info", "debug_log"],
            "propagate": True,
        },
        "gunicorn.error": {
            "handlers": ["console", "error_file"],
            "level": "INFO",
            "propagate": True,
        },
        "gunicorn.access": {
            "handlers": ["console", "access_file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
