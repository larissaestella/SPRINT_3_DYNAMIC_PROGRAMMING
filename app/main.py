from ordenacao import merge_sort
from heap_k_elementos import get_k_maiores, get_k_menores
from bst_autocomplete import BST
from utils import carregar_dados

def mostrar_menu():
    print("\n=== APP MECÂNICO ===")
    print("1 - Ordenar por preço (crescente/decrescente)")
    print("2 - K maiores ou menores por estoque")
    print("3 - Autocomplete por nome da peça")
    print("0 - Sair")

def main():
    data = carregar_dados()

    while True:
        mostrar_menu()
        op = input("Escolha a opção: ")

        if op == "1":
            while True:
                ordem = input("Ordenar por [c]rescente ou [d]ecrescente? ").lower()
                if ordem in ("c", "d"):
                    break
                else:
                    print("❌ Opção inválida! Digite apenas 'c' para crescente ou 'd' para decrescente.")

            try:
                quantidade = int(input("Quantos produtos deseja ver? "))
                ordenado = merge_sort(data, key="preco", reverse=(ordem == "d"))
                for item in ordenado[:quantidade]:
                    print(f"{item['nome']} - Estoque: {item['estoque']} - R${item['preco']}")
            except ValueError:
                print("❌ Quantidade inválida. Digite um número inteiro.")


        elif op == "2":
            while True:
                tipo = input("Buscar [m]aiores ou me[n]ores estoques? ").lower()
                if tipo in ("m", "n"):
                    break
                else:
                    print("❌ Opção inválida! Digite apenas 'm' para maiores ou 'n' para menores.")

            try:
                k = int(input("Quantos produtos? "))
                if tipo == "m":
                    resultado = get_k_maiores(data, key="estoque", k=k)
                else:
                    resultado = get_k_menores(data, key="estoque", k=k)

                for item in resultado:
                    print(f"{item['nome']} - R${item['preco']} - Estoque: {item['estoque']}")
            except ValueError:
                print("❌ Quantidade inválida. Tente novamente.")


        elif op == "3":
            bst = BST()
            for item in data:
                bst.insert(item["nome"])

            while True:
                texto = input("Digite parte do nome da peça: ").strip()
                if texto:
                    break
                else:
                    print("❌ Entrada inválida! Digite pelo menos uma letra para buscar.")

            sugestoes = bst.search_prefix(texto)
            print("Sugestões:")
            for s in sugestoes:
                print("-", s)


        elif op == "0":
            print("\nSaindo do sistema...")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
