import json
import logging
import logging.config
import time

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "txt": {
            "format": "[%(asctime)s.%(msecs)03d][%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
        "jsonl": {
            "format": json.dumps(
                {
                    "timestamp": "%(asctime)s.%(msecs)03d",
                    "process": "%(process)d",
                    "thread": "%(thread)d",
                    "logger": "%(name)s",
                    "level": "%(levelname)s",
                    "source": "%(pathname)s:%(lineno)d",
                    "message": "%(message)s",
                }
            ),
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "filters": {},
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "event.log",
            "formatter": "jsonl",
            "level": "DEBUG",
            "filters": [],
        },
        "stream": {
            "class": "logging.StreamHandler",
            "formatter": "txt",
            "level": "DEBUG",
            "filters": [],
        },
    },
    "loggers": {
        "client": {
            "handlers": ["file", "stream"],
            "level": "DEBUG",
            "propagate": True,
        },
        "worker": {
            "handlers": ["file", "stream"],
            "level": "DEBUG",
            "propagate": True,
        },
        "protocol": {
            "handlers": ["file", "stream"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
logging.Formatter.converter = time.gmtime
logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(id: str) -> logging.Logger:
    return logging.getLogger(id)


class Config:
    def __init__(self, serial_port: str, baud_rate: int, encoding: str) -> None:
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.encoding = encoding
