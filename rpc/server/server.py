import asyncio

import services
from handler import rpc_handler
from settings import logging


async def main():
    __HOST = "127.0.0.1"
    __PORT =  5000

    # Inicia um socket server
    server = await asyncio.start_server(rpc_handler, __HOST, __PORT)

    # Nome endereço do servidor
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    logging.info(f"Servidor escutando em: {addrs}")

    async with server:
        # Passa a aceitar conexões
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
