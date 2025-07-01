import asyncio
import random

from registry import rpc


@rpc
def say_hello(to):
    return f"Hello, {to}!"

@rpc
async def say_bye(to):
    await asyncio.sleep(random.uniform(0, 1))
    return f"Bye, {to}!"

def internal():
    return f"{say_hello()} {say_bye}"
