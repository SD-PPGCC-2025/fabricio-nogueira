# Mestrado UFG - Sistemas distribuídos

## Simulação de Deadlock em sistemas distribuídos

Objetivo: demonstrar dois cenários clássicos em sistemas distribuídos envolvendo **deadlock**:

1. Um cenário com **tratamento e prevenção de deadlock**
2. Um cenário **sem tratamento**, resultando em **deadlock real**

A aplicação é composta por dois serviços (`Service A` e `Service B`) que simulam o uso de **recursos compartilhados** com bloqueios (`locks`) e realizam chamadas remotas via **RPC**.

---

## Tecnologias Utilizadas

- Python
- [Nameko](https://www.nameko.io/) – framework para microserviços
- RabbitMQ – broker de mensagens
- `eventlet` – para controle de timeout e concorrência
- `threading` – para simular acesso a recursos com locks

---

## Conceitos Abordados

- Deadlock em sistemas distribuídos
- Locks e recursos compartilhados
- Timeout para prevenção de deadlocks
- Retry com limitação para evitar loops infinitos
- Comunicação RPC entre serviços

---

## Cenário 1 – Com Tratamento de Deadlock

### Comportamento Esperado

- Cada serviço tenta adquirir um lock (recurso).
- Caso o outro serviço já tenha o recurso, espera com **timeout controlado**.
- Em caso de demora (possível deadlock), um **timeout** é disparado.
- A execução é **interrompida com segurança**, liberando os locks e retornando uma mensagem clara ao cliente.
- Há também uma lógica de **retry limitada** para novas tentativas.

### Técnicas Aplicadas

| Técnica         | Função                                         |
|-----------------|------------------------------------------------|
| `threading.Lock` | Simula recurso compartilhado                  |
| `eventlet.Timeout(...)` | Impede bloqueio indefinido (deadlock)         |
| `retry`         | Evita laço infinito de chamadas recursivas    |
| `finally: release()` | Garante liberação do recurso                  |

### Resultado

- O sistema **identifica e evita** o deadlock.
- Os serviços continuam respondendo corretamente.
- O usuário recebe uma resposta informando o timeout.

---

## Cenário 2 – Sem Tratamento de Deadlock

### Comportamento Esperado

- Os serviços realizam chamadas recursivas e bloqueiam recursos mutuamente.
- Como não há timeout ou retry, os serviços entram em **deadlock real**.
- As threads ficam **presas** esperando indefinidamente.
- Nenhuma resposta é enviada ao cliente.

### Técnicas Aplicadas

| Técnica            | Função                                  |
|--------------------|------------------------------------------|
| `threading.Lock`   | Simula acesso exclusivo a recursos       |
| (sem timeout)      | Deadlock ocorre por espera indefinida    |
| (sem retry)        | Não há tentativa de recuperação          |

### Resultado

- O sistema trava completamente.
- É necessário reiniciar os serviços manualmente.
- Demonstra um **deadlock clássico** distribuído.

---

## Setup

### Requisitos Python

Serviços desenvolvidos em Python, scripts e automações.

- [Poetry](https://python-poetry.org/docs/#installation) versão 1.5.1 ou superior
  - Opcional: Plugin `poetry self add poetry-dotenv-plugin`. No diretório corrente, carrega o arquivo _.env_ setando as variáveis de ambiente ao executar `poetry run ...`
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) Python package project template.

## Novos serviços

Crie novos serviços utilizando nosso template.

Mais informações no readme do diretório _./template_

Na raiz do projeto, execute:

```bash
cookiecutter template/ -o services/
```

## Execução

### Requisitos

- [Docker](https://docs.docker.com/desktop/install/linux-install/)
- [Docker-compose](https://docs.docker.com/compose/install/linux/)

Para executar o projeto, utilizando o docker-compose, o primeiro passo é executar o script de preparação, para gerar o arquivo _.env_ nos serviços, contendo as variáveis de ambiente necessárias para a execução.

```bash
./prepare.sh
```

Subir todos os serviços:

```bash
docker-compose up -d
```

Subir serviços específicos:

```bash
docker-compose up <nome-do-serviço> -d
```

IMPORTANT: Os serviços utilizam rpc para comunicação, o [Nameko](https://www.nameko.io/) é o framework responsável. Ele utiliza o protocolo [AMQP](https://www.rabbitmq.com/tutorials/amqp-concepts.html) que é executado atraves do [RabbitMQ](https://www.rabbitmq.com/documentation.html). Dessa forma, os serviços devem ser executados, juntamente com uma instância acessivel do RabbitMQ.
