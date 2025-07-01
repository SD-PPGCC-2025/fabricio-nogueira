import functools

from settings import logs


def trace(_class: str, _method: str, action: str, **zwargs):
    def decorator_trace(func):
        @functools.wraps(func)
        def wrapper_trace(*args, **kwargs):
            log_params = dict(_class=_class, _method=_method, **zwargs)
            logs.init(**log_params, action=action)
            value = func(*args, **kwargs)
            logs.end(**log_params)
            return value

        return wrapper_trace

    return decorator_trace
