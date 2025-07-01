from pytz import timezone
from datetime import datetime

FORMAT = "%d-%m-%Y %H:%M:%S"


def now_utc() -> str:
    _now = datetime.now(timezone("UTC"))
    return _now.strftime(FORMAT)


def now() -> str:
    _now = datetime.now(timezone("America/Sao_Paulo"))
    return _now.strftime(FORMAT)
