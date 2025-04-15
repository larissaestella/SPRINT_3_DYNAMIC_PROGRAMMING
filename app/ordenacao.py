def merge_sort(lista, key, reverse=False):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], key, reverse)
    direita = merge_sort(lista[meio:], key, reverse)

    return mesclar(esquerda, direita, key, reverse)

def mesclar(esquerda, direita, key, reverse):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        condicao = esquerda[i][key] < direita[j][key]
        if reverse:
            condicao = not condicao

        if condicao:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
