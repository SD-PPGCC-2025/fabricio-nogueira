import asyncio
import json

async def call(func_name, args=None, kwargs=None):
    args = args or []
    kwargs = kwargs or {}

    reader, writer = await asyncio.open_connection('127.0.0.1', 5000)

    request = {
        'func': func_name,
        'args': args,
        'kwargs': kwargs
    }

    writer.write(json.dumps(request).encode('utf-8'))
    await writer.drain()

    data = await reader.read(4096)
    writer.close()
    await writer.wait_closed()

    response = json.loads(data.decode('utf-8'))
    return response

