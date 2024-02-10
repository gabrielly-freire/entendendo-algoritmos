def busca_menor(lista):
    menor = lista[0]
    indice = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return indice

def ordenacao_por_selecao(lista):
    lista_ordenada = []

    for i in range(0, len(lista)):
        menor = busca_menor(lista)
        lista_ordenada.append(lista.pop(menor))

    return lista_ordenada

lista = [8, 2, 5, 6, 4, 9]

print(ordenacao_por_selecao(lista))