import heapq

def obter_k_maiores(dados, chave, k):
    return heapq.nlargest(k, dados, key=lambda x: x[chave])

def obter_k_menores(dados, chave, k):
    return heapq.nsmallest(k, dados, key=lambda x: x[chave])
