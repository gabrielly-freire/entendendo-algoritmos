# Capítulo 3 - Recursão

O capítulo em questão aborda: recursão e pilha.

## Recursão

Recursão é uma abordagem mais elegante para a resolução de problemas, na qual a função chama a si mesma.

É importante ressaltar que essa metodologia não traz benefícios em relação ao desempenho de um programa, mas pode tornar a resolução mais clara.

### Caso-base e caso recursivo

Toda função recursiva possui duas partes:
- **Caso recursivo**: quando a função chama a si mesma.
- **Caso-base**: quando a função não se chama novamente, evitando um loop infinito.

## Pilha

Uma pilha é uma estrutura de dados que oferece duas operações fundamentais: push (inserir, que só insere no topo) e pop (remover e ler).

### Pilha de Chamada

Ao chamar uma função, um espaço na memória do computador é reservado para ela. Este espaço é utilizado para armazenar as variáveis associadas à função.

Esses espaços na memória são organizados em uma estrutura de pilha, onde cada função é empilhada uma sobre a outra (a função "principal" e a função chamada).

Quando uma função é chamada dentro de outra, a função chamadora entra em um estado parcialmente completo, ficando pausada e com todas as suas variáveis salvas.

Enquanto a função chamada estiver em execução, os espaços na memória são empilhados. Após a conclusão da função chamada, o espaço é liberado, e a função chamadora retoma a execução de suas instruções.

## Exercícios
- 3.1 - A função `sauda` foi inicialmente chamada, armazenando o valor "Maggie" na variável `nome`. Em seguida, a função `sauda` chamou a função `sauda_2`, pausando temporariamente seu estado. A função `sauda_2` também armazenou "Maggie" na variável `nome`. Esse valor permanece armazenado enquanto a função está em execução. Após a conclusão da função `sauda_2`, seu espaço na memória é desempilhado, e a função `sauda` retoma sua execução, continuando suas instruções.
- 3.2 - As pilhas serão empilhadas infinitamente; eventualmente, algum erro por falta de memória será lançado.
