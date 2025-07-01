import asyncio
from threading import Lock

from registry import rpc
from settings import logging
from queue import Queue

queue = Queue()
lock = Lock()

@rpc
async def queue_add(message):
    global queue
    with lock:
        queue.put(message)

@rpc
async def queue_get():
    global queue
    with lock:
        return queue.get(block=False)

