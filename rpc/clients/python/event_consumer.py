import asyncio
import random
import time

from rpc import call

async def main():
    while True:
        queue = await call('queue_get')
        queue_result = queue.get('result')

        if queue_result:
            print(queue_result)
            await call('event_update', [random.randint(1, 1000)])

        time.sleep(random.uniform(0, 1))

if __name__ == '__main__':
    asyncio.run(main())
