import asyncio
from threading import Lock

from registry import rpc
from settings import logging

time = 0
lock = Lock()

@rpc
async def event_increment():
    global time
    with lock:
        time += 1

    return time

@rpc
async def event_update(received_time):
    global time
    with lock:
        time = max(time, received_time) + 1

    return time
