def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]
        if(chute == item):
            return True
        elif(chute > item):
            alto = meio - 1 # reduz a zona de pesquisa pela esquerda
        else:
            baixo = meio + 1 # reduz a zona de pesquisa pela direita
    return False

lista = [1, 2, 3, 4, 5, 6, 8, 10]
item = 1

resultado = busca_binaria(lista, item)
print("O {} está na lista: {}".format(item, resultado))

