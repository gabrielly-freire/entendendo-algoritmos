# Capítulo 1 - Introdução a Algoritmos

O capítulo em questão aborda: pesquisa binária e notação Big O.

## Tipos de Pesquisa
Existem diferentes formas de resolver um problema. Entretanto, algumas são bem mais otimizadas que outras, o que diz respeito à complexidade de algoritmos, ou seja, eficiência de um algoritmo em termos de tempo e memória.

## Pesquisa Linear/Sequencial
Consiste em uma busca que pesquisa elemento por elemento em uma lista até encontrar o elemento desejado.

## Pesquisa Binária
Consiste em uma maneira mais otimizada de pesquisar um elemento específico em uma lista de elementos.

A lista de elementos precisa estar organizada em ordem crescente ou decrescente. O funcionamento da busca binária é o seguinte:
- O primeiro elemento que será verificado é o elemento central;
- Diante disso, são feitas algumas comparações sobre esse elemento:
  - É igual ao elemento desejado;
  - É menor que o elemento desejado;
  - É maior que o elemento desejado.
- A partir disso, é possível cortar pela metade a quantidade de elementos que serão analisados.
- Esses passos são seguidos até encontrar o elemento ou até o fim da lista;

Perceba que a quantidade de elementos que serão verificados é log2 x, em que x é a quantidade de elementos da lista.

## Notação Big O
Essa notação diz respeito a quão rápida é a execução de um algoritmo. A notação Big O permite comparar o número de operações executadas. É importante ressaltar que o Big O sempre leva em consideração o pior caso. Por exemplo, na busca linear, é possível que um elemento seja encontrado na primeira verificação, esse é o melhor caso. Entretanto, também é possível que ele seja encontrado por último, o pior caso.

### Exemplos comuns de tempo de execução Big O
- O(log n) - tempo logarítmico (busca binária).
- O(n) - tempo linear (busca linear).
- O(n * log n) - (ordenação rápida).
- O(n²) - (ordenação por seleção).
- O(n!) - tempo fatorial (algoritmo do caixeiro viajante).

> A rapidez de um algoritmo não é medida em tempo, mas sim no número de operações executadas.

## Caixeiro Viajante

O caixeiro viajante Opus precisa ir em cinco cidades. Mas ele quer passar por todas as cidades percorrendo uma distância mínima. Para isso, temos que analisar cada ordem possível de cidades para visitar, somar todas as distâncias.

| Cidades | Operações | 
|----------|:--------:|
| 6 | 720 |
| 7 | 5040 |
| 8 | 40320 |
| ... | ... |
| 15 |  1307674368000 |

O número de operações aumenta drasticamente.

## Exercícios
1.1 - 7 etapas.
1.2 - 8 etapas.
1.3 - O(log n).
1.4 - O(n).
1.5 - O(n).
1.6 - ??
