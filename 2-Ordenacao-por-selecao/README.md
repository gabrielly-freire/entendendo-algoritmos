# Capítulo 2 - Ordenação por Seleção

O capítulo em questão aborda arrays, listas encadeadas e um algoritmo de ordenação.

## Arrays e Listas Encadeadas

Existem duas formas de armazenar uma lista de elementos na memória.

### Arrays

No array, os itens são armazenados um ao lado do outro.
- **Vantagem**
  - Fácil acesso
- **Desvantagens**
  - Dificuldade na inserção
  - Problemas de alocação de memória (necessita de bloco contínuo para o armazenamento)
  - Dificuldade na deleção de itens

### Listas Encadeadas

Na lista encadeada, os itens são armazenados arbitrariamente na memória.
- Cada item armazena o endereço do próximo item da lista, ou seja, estão todos interligados.
- **Vantagens**
  - Fácil inserção de itens (pode falhar se não houver espaço suficiente)
  - Facilidade na deleção de itens
- **Desvantagem**
  - Dificuldade de acesso, é necessário verificar um a um

## Ordenação por Seleção

A ordenação por seleção consiste em um método de ordenação em que se selecionam os menores elementos e os insere em uma nova lista até ter uma lista totalmente ordenada. 
Esse é um algoritmo eficaz, porém não é rápido, tendo um tempo de execução de O(n²).

## Exercícios

- 2.1 - Lista encadeada, pois a inserção é frequente e a leitura não é tão frequente.
- 2.2 - Lista encadeada, pois a inserção e deleção de itens são constantes e a leitura precisa ser sequencial.
- 2.3 - Arrays, pois, nesses casos, o acesso fácil a elementos é importante.
- 2.4 - O problema é onde inserir,  no array, é preciso mover os itens para poder inserir na posição adequada da ordem sequencial.
- 2.5 - É bem mais rápido para acessar os itens e faz uso da lista encadeada para inserir e deletar itens, ou seja, tem desempenho igual à lista encadeada nesse aspecto.
