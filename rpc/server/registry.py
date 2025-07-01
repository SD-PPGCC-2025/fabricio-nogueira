import inspect
from settings import logging

registry = {}

def rpc(func):
    func_name = func.__name__
    is_async = inspect.iscoroutinefunction(func)

    # Registrar função no dicionário
    registry[func_name] = func

    tipo = "assíncrona" if is_async else "síncrona"
    logging.info(f"Função registrada: '{func_name}' ({tipo})")

    return func
