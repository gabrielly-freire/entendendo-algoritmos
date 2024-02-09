def busca_sequencial(lista, item):
    for i in lista:
        if item == i:
            return True
    return False 


lista = [2, 3, 4, 6, 8, 5]
item = 8

resultado = busca_sequencial(lista, item)
print("O {} está na lista: {}".format(item, resultado))
