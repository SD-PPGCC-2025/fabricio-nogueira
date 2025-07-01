import logging
import threading

import eventlet
import time
from nameko.rpc import rpc, RpcProxy


class ServiceAService:
    """
    Serviço A
    """
    name = "service_a"

    service_b = RpcProxy("service_b")

    # Simula recursos compartilhados (A e B)
    lock_a = threading.Lock()

    @rpc
    def deadlock_fixed(self, retry=3):
        # Evita laços infinitos (limita o número de tentativas de recuperação)
        if retry <= 0:
            logging.info("[A] Número máximo de tentativas atingido.")
            return "A: abortado após múltiplas tentativas"

        acquired = ServiceAService.lock_a.acquire(timeout=2)
        if not acquired:
            logging.info("[A] Falha ao adquirir recurso A")
            return "A: recurso indisponível"

        try:
            logging.info("[A] Recurso A adquirido. Chamando B...")
            time.sleep(1)

            # Captura o timeout para lidar com o deadlock
            try:
                # Define um tempo máximo de espera para detectar o possível deadlock
                with eventlet.Timeout(2):
                    return self.service_b.deadlock_fixed(retry=retry - 1)
            except eventlet.Timeout:
                logging.info("[A] Timeout alcançado. Deadlock suspeito.")
                return "A: deadlock detectado"

        except Exception as e:
            logging.error(f"[A] Deadlock detectado ou erro na chamada: {e}")
            return "A: deadlock detectado"
        # Garante liberação de recursos mesmo em falhas
        finally:
            ServiceAService.lock_a.release()
            logging.info("[A] Recurso A liberado.")

    @rpc
    def hello(self):
        return "Olá do serviço A"

    @rpc
    def deadlock(self):
        acquired = ServiceAService.lock_a.acquire()
        if not acquired:
            logging.info("[A] Falha ao adquirir recurso A")
            return "A: recurso indisponível"

        try:
            logging.info("[A] Recurso A adquirido. Chamando B...")
            time.sleep(1)  # Simula atraso

            # Sem timeout e sem retry → Deadlock ocorre aqui
            return self.service_b.deadlock()

        except Exception as e:
            logging.error(f"[A] Erro inesperado: {e}")
            return "A: erro"

        finally:
            ServiceAService.lock_a.release()
            logging.info("[A] Recurso A liberado.")
