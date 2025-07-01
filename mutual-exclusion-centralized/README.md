# Exclusão multua: Algoritmo Centralizado
A ideia é bem intuitiva: existe um coordenador central que atua como um "porteiro" do recurso crítico. Todo processo que quiser acessar o recurso deve pedir permissão ao coordenador. Ele mantém o controle e concede ou nega o acesso com base na disponibilidade.

## Estrutura do Algoritmo

### Entidades:
Coordenador (C): processo especial que decide quem entra na seção crítica (SC).

Processos requisitantes (P₁, P₂, ..., Pₙ): processos distribuídos que querem acessar o recurso crítico.

Passos do Algoritmo

1. Requisição:
- Um processo 𝑃𝑖 envia uma mensagem REQUEST para o coordenador.

2. Decisão:
- Se nenhum outro processo está na seção crítica, o coordenador responde com GRANT.
- Caso contrário, ele enfileira o pedido.

3. Uso da Seção Crítica:
- O processo 𝑃𝑖 entra na seção crítica após receber o GRANT.

4. Liberação:
- Quando termina, o processo envia RELEASE ao coordenador.
- O coordenador então concede GRANT ao próximo processo na fila (se houver).

## Complexidade
Mensagens por entrada na SC:

- REQUEST → Coordenador
- GRANT ← Coordenador
- RELEASE → Coordenador

Total = 3 mensagens

Latência: baixa (apenas uma ida e volta ao coordenador).

## Vantagens
- Simples de entender e implementar
- Baixo número de mensagens por entrada na seção crítica (eficiente em redes pequenas)
- Coordenador pode implementar políticas de prioridade, fairness, timeout, etc.

## Desvantagens
- Ponto único de falha (SPOF): se o coordenador falhar, o sistema trava.
- Gargalo de desempenho: o coordenador pode virar um bottleneck se muitos processos fizerem requisições simultaneamente.
- Não é escalável para sistemas com muitos nós ou tráfego intenso.

## Aplicações Típicas
- Útil para ambientes controlados ou pequenos clusters
- Situações com baixa concorrência pelo recurso
- Laboratórios, simulações ou ambientes onde a tolerância a falhas não é crítica

## Exemplo Ilustrativo
Imaginando 3 processos (P1, P2, P3) e um coordenador (C):

1. P1 → C: REQUEST
2. C → P1: GRANT
3. P1 entra na SC
4. P2 → C: REQUEST
5. C adiciona P2 à fila
6. P1 → C: RELEASE
7. C → P2: GRANT
8. P2 entra na SC...

## Considerações Adicionais
- Pode-se adicionar backup do coordenador com heartbeat e eleição automática para resolver a questão do SPOF (isso já entra em outro tema do livro, como eleição de líder).
- O coordenador pode armazenar estado persistente para recomeçar após falha.
- Pode-se implementar timeout no coordenador para evitar deadlocks se um processo não liberar a SC.

## Conclusão
O algoritmo centralizado é uma boa introdução à exclusão mútua em sistemas distribuídos, ideal para entender os fundamentos de coordenação e sincronização. No entanto, sua fragilidade diante de falhas e limitações de escalabilidade tornam-no impraticável para sistemas distribuídos reais de grande porte.