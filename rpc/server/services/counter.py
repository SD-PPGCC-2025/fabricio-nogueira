import asyncio
from threading import Lock

from registry import rpc

counter = 0
lock = Lock()

@rpc
async def update_counter():
    global counter
    with lock:
        counter += 1

    return counter
