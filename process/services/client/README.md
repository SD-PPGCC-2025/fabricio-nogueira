# Local RPC calls

Execute localmente chamadas RPC aos serviços.

Python version: 3.9.x

## Setup

Instale as dependências do projeto

```bash
poetry install
```

No contexto do cluster em que irá executar a função, faça o [port forward](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod) do broker:

```bash
kubectl port-forward service/broker -n sre :5672
```

Atualize o arquivo `.env` adicionando a porta local, gerada no port forward, na variável `RABBITMQ_PORT`.

Execute o shell

```bash
poetry run nameko shell --config ./config.yaml
```

As chamadas podem ser [executadas pelo terminal](https://nameko.readthedocs.io/en/stable/cli.html#interacting-with-running-services)

Ex.:

```bash
n.rpc.<service>.<method>(...)
```