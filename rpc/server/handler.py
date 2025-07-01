from asyncio import StreamReader, StreamWriter
import json
import inspect
from settings import logging

from registry import registry

async def rpc_handler(reader: StreamReader, writer: StreamWriter):
    # Endereço remoto ao qual o soquete está conectado - host e porta
    addr = writer.get_extra_info('peername')
    logging.info(f"Conexão recebida de {addr}")

    try:
        # Lê até 4096 bytes do stream de dados
        data = await reader.read(4096)
        message = data.decode()

        try:
            # Comunicação via json
            request = json.loads(message)
        except json.JSONDecodeError:
            response = {"error": "Requisição inválida: JSON malformado"}
            writer.write(json.dumps(response).encode())
            await writer.drain()
            writer.close()
            return

        func_name = request.get("func")
        args = request.get("args", [])
        kwargs = request.get("kwargs", {})

        func = registry.get(func_name)

        if not func:
            response = {"error": f"Função '{func_name}' não registrada"}
        else:
            try:
                if inspect.iscoroutinefunction(func):
                    result = await func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)

                response = {"result": result}
            except Exception as err:
                response = {"error": f"Erro ao executar '{func_name}': {str(err)}"}

        writer.write(json.dumps(response).encode())
        await writer.drain()

    except Exception as err:
        logging.error(f"Erro geral na conexão com {addr}: {err}")
    finally:
        writer.close()
        await writer.wait_closed()
        logging.info(f"Conexão encerrada com {addr}")
