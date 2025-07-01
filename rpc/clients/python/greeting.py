import asyncio

from rpc import call


async def main():
    print(await call('say_hello', ['David']))
    print(await call('say_bye', ['Richard']))
    print(await call('say_good_evening', ['Roger']))

if __name__ == '__main__':
    asyncio.run(main())
