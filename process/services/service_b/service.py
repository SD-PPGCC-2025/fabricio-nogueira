import logging
import threading
import time

import eventlet
from nameko.rpc import rpc, RpcProxy


class ServiceBService:
    """
    Serviço B
    """
    name = "service_b"

    service_a = RpcProxy("service_a")

    lock_b = threading.Lock()

    @rpc
    def deadlock_fixed(self, retry=3):
        if retry <= 0:
            logging.info("[B] Número máximo de tentativas atingido.")
            return "B: abortado após múltiplas tentativas"

        acquired = ServiceBService.lock_b.acquire(timeout=2)
        if not acquired:
            logging.info("[B] Falha ao adquirir recurso B")
            return "B: recurso indisponível"

        try:
            logging.info("[B] Recurso B adquirido. Chamando A...")
            time.sleep(1)

            try:
                with eventlet.Timeout(2):  # Agora lança exceção se demorar
                    return self.service_a.deadlock_fixed(retry=retry - 1)
            except eventlet.Timeout:
                logging.info("[B] Timeout alcançado. Deadlock suspeito.")
                return "B: deadlock detectado"

        except Exception as e:
            logging.error(f"[B] Deadlock detectado ou erro na chamada: {e}")
            return "B: deadlock detectado"

        finally:
            ServiceBService.lock_b.release()
            logging.info("[B] Recurso B liberado.")

    @rpc
    def hello(self):
        return "Olá do serviço B"

    @rpc
    def deadlock(self):
        acquired = ServiceBService.lock_b.acquire()
        if not acquired:
            print("[B] Falha ao adquirir recurso B")
            return "B: recurso indisponível"

        try:
            print("[B] Recurso B adquirido. Chamando A...")
            time.sleep(1)  # Simula atraso
            # Sem timeout e sem retry → Deadlock ocorre aqui
            return self.service_a.deadlock()
        except Exception as e:
            print(f"[B] Erro inesperado: {e}")
            return "B: erro"
        finally:
            ServiceBService.lock_b.release()
            print("[B] Recurso B liberado.")
