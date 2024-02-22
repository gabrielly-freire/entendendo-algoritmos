# Capítulo 5 - Tabela hash

No capítulo em questão é abordado a estrutura de dados tabela hash. Também conhecido como tabela de dispersão, dicionário, mapa hash, mapa, entre outros.

## Tabela hash
A tabela hash é uma estrutura de dados que associa chaves de pesquisa a valores. É uma coleção de itens que são armazenados de forma que a localização de um determinado item seja diretamente acessível. A ideia é que a função hash é usada para mapear a chave para o valor desejado. A função hash recebe a chave como entrada e retorna um índice na tabela hash onde o valor desejado pode ser encontrado.

Ela é eficiente para operações de inserção, remoção e busca. A complexidade de tempo dessas operações é O(1) em média. No pior caso, a complexidade de tempo é O(n).

O pior caso ocorre quando tem muitas colisões. Portanto, uma boa função hash distribui os itens de forma uniforme pela tabela hash, assim, evitando colisões.

### Colisões
Colisões são situações onde dois ou mais itens são mapeados para o mesmo índice da tabela hash. Uma forma de resolver colisões é usar uma lista encadeada para armazenar os itens que colidem. Entretando, se ocorrer muitas colisões, a complexidade de tempo das operações pode se tornar O(n) por causa que a lista encadeanda tem busca linear.

Outra forma de resolver colisões é expandir a tabela hash. Entretanto, essa abordagem pode ser custosa.

### Fator de carga
O fator de carga é a razão entre o número de itens armazenados e o tamanho da tabela hash. Se o fator de carga for muito alto, a tabela hash terá muitas colisões. Se o fator de carga for muito baixo, a tabela hash terá muita memória desperdiçada.

Idealmente, recomenda-se que o fator de carga seja 0.7. Ou seja, a tabela hash deve estar 70% cheia. Assim, é realizada a operação de redimensionamento da tabela hash.

### Desempenho
A tabela hash tem desempenho O(1) para operações de inserção, remoção e busca. Entretanto, no pior caso, a complexidade de tempo é O(n).
Note que no caso médio o tabela hash tem um desempenho bem melhor que a busca sequencial e a busca binária.

### Exemplos de uso de tabela hash
- Lista de contatos: nome -> número de telefone
- Cache de sites: URL -> conteúdo da página
- Resolução DNS: nome do host -> endereço IP

### Implementação
Raramente é necessário implementar uma tabela hash do zero. A maioria das linguagens de programação já possuem uma implementação de tabela hash. Por exemplo, em Python, a classe `dict` é uma tabela hash.