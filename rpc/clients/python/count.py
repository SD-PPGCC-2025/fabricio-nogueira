import asyncio
import random
import time

from rpc import call

async def main():
    while True:
        time.sleep(random.uniform(0, 1))
        print(await call('update_counter'))

if __name__ == '__main__':
    asyncio.run(main())
