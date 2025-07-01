import logging
from datetime import datetime

from pythonjsonlogger import jsonlogger

from settings.settings import ProcessType


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(
            log_record, record, message_dict
        )
        log_record["service"] = "service_b"
        if not log_record.get("timestamp"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname

        if not log_record.get("message"):
            del log_record["message"]


def init(_class, _method, action="", **kwargs):
    logging.info(
        {
            "class": _class,
            "method": _method,
            "process": ProcessType.INIT,
            "action": action,
            **kwargs,
        }
    )


def end(_class, _method, **kwargs):
    logging.info(
        {
            "class": _class,
            "method": _method,
            "process": ProcessType.END,
            **kwargs,
        }
    )


def error(_class, _method, **kwargs):
    logging.error(
        {
            "class": _class,
            "method": _method,
            "process": ProcessType.ERROR,
            **kwargs,
        }
    )
