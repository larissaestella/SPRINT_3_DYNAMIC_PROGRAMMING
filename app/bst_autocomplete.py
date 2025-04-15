class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        def _inserir(no, valor):
            if not no:
                return No(valor)
            if valor < no.valor:
                no.esquerda = _inserir(no.esquerda, valor)
            else:
                no.direita = _inserir(no.direita, valor)
            return no
        self.raiz = _inserir(self.raiz, valor)

    def buscar_por_prefixo(self, prefixo):
        resultados = []

        def _em_ordem(no):
            if no:
                _em_ordem(no.esquerda)
                if no.valor.lower().startswith(prefixo.lower()):
                    resultados.append(no.valor)
                _em_ordem(no.direita)

        _em_ordem(self.raiz)
        return resultados[:5]  # Limita a 5 sugestões
