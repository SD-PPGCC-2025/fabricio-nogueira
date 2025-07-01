# RPC - Remote Procedure Call

RPC é um modelo de comunicação entre processos em sistemas distribuídos que permite que um programa chame uma função (ou procedimento) em outro computador como se fosse local. O principal objetivo do RPC é abstrair a complexidade da comunicação entre máquinas, fornecendo uma interface simples para a execução de chamadas remotas.

## Componentes em uma comunicação RPC

- Stub (cliente e servidor):
    - O cliente stub representa a função remota no lado cliente.
    - O servidor stub traduz a chamada recebida e a executa no servidor.
- Serialização (marshalling):
    - Os parâmetros da função são convertidos em um formato transmissível pela rede.
- Transporte:
    - A chamada é enviada ao servidor via rede.
- Execução remota:
    - O servidor recebe, desserializa os parâmetros, executa a função e serializa o resultado.
- Resposta:
    - O resultado volta pelo mesmo caminho ao cliente.
- Deserialização (unmarshalling):
    - O cliente recebe e reconstrói o valor de retorno como se fosse uma chamada local.

## Estrutura do projeto

### Server

Cria o servidor remoto e registra os métodos.

### Clients

Escritos em diferentes linguages, se conectam ao servidor e acessam os métodos remotos.