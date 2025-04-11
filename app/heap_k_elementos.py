import heapq

def get_k_maiores(data, key, k):
    return heapq.nlargest(k, data, key=lambda x: x[key])

def get_k_menores(data, key, k):
    return heapq.nsmallest(k, data, key=lambda x: x[key])
