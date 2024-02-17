# Capítulo 4 - Quicksort

No capítulo em questão é abordado a técnica dividir para conquistar e o algoritmo de ordenação quicksort.

## Dividir para conquistar
É uma técnica de resolução de problema que pode ser utilizada em qualquer problema. Ela possui os seguintes passo:
1. Descubrir o caso-base
2. Descubrir como reduzir o problema até que ele se torne o casa-base

Portanto, a ideia por traz dessa técnica é a divisão em problemas menores.

## Quicksort
Esse é o algoritmo de ordenação mais rápido que existe ele possui a complexidade de O(n log n) e faz uso da técnica dividir para conquistar.

A ideia por traz do algoritmo é a seguinte:
1. Escolher um elemento do array, que será o pivô
2. Dividir o array em dois sub-arrays, um com todos os elementos menores que o pivô e outro com todos os elementos maiores que o pivô
3. Ordenar os sub-arrays
4. Juntar os sub-arrays (a parte menor que o pivô + o pivô + a parte maior que o pivô)
5. Retornar o array ordenado

A complexidade no pior caso(quando a divisão em partes for muito desigual) do quicksort é O(n^2), mas no caso melhor e no médio é O(n log n).

## Mergesort
Também é um algoritmo de ordenação que faz uso da técnica dividir para conquistar. 

O mergesort não faz uso de uma estratégia de escolha do pivô, ele simplesmente divide o array em duas partes iguais e ordena essas partes. Depois ele junta as partes ordenadas. Uma desvantagem do mergesort é que ele utiliza mais memória que o quicksort.

A ideia por traz do mergesort é a seguinte:
1. Dividir o array em duas partes iguais
2. Ordenar as duas partes
3. Juntar as duas partes (adequando a ordem dos elementos)
4. Retornar o array ordenado

A complexidade do mergesort também é O(n log n).

## Quicksort vs. mergesort
Por mais que ambos os algoritmos possuam a mesma complexidade, o quicksort é mais rápido que o mergesort. Isso se deve ao fato de que o quicksort faz menos comparações que o mergesort.
Portanto, há casos que a notação Big O é relativa quando se trata de comparação de algoritmos de ordenação.
