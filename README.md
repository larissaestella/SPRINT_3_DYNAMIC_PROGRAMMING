
# CHALLENGE FIAP - SPRINT 3: APP MECÂNICO

    Sistema em Python desenvolvido para mecânicos consultarem peças automotivas utilizando diferentes algoritmos de busca e ordenação, com base em uma API simulada da Rede Âncora.

---

## 📚 Funcionalidades

O aplicativo é executado via terminal e oferece as seguintes funcionalidades:

### 1. 🔍 Ordenação de Produtos por Preço
- Permite ordenar os produtos por preço **crescente** ou **decrescente**.
- Utiliza o algoritmo **Merge Sort** implementado manualmente.

### 2. 📊 K Maiores ou Menores Estoques
- Mostra os **K produtos com maior ou menor quantidade em estoque**.
- Implementado com **Heap Máximo/Mínimo** para maior eficiência.

### 3. 🧠 Autocomplete com Árvore Binária
- Sugere nomes de produtos à medida que o usuário digita.
- Usa **Árvore Binária de Busca (BST)** para retornar pelo menos 5 sugestões de autocomplete.

---

## 📁 Estrutura de Arquivos

```
app_mecanico/
│
├── main.py                     # Arquivo principal para rodar o app
├── ordenacao.py                # Contém o algoritmo Merge Sort
├── heap_k_elementos.py         # Funções de heap para K maiores/menores
├── bst_autocomplete.py         # Implementação da Árvore de Busca Binária
├── utils.py                    # Carregamento de dados JSON
├── data.json                   # Catálogo de produtos (dados simulados)
└── README.md                   # Este arquivo
```

---

## ▶️ Como Rodar o Projeto

1. **Clone o repositório ou baixe os arquivos** em sua máquina.
2. Verifique se você tem o Python 3 instalado.
3. No terminal, navegue até a pasta onde está o projeto:
   ```bash
   cd caminho/para/SPRINT_3_DYNAMIC_PROGRAMMING/app
   ```
4. Execute o programa:
   ```bash
   python main.py
   ```

---

## 📌 Exemplo de Uso

Ao rodar o programa, o menu será exibido:
```
=== APP MECÂNICO ===
1 - Ordenar por preço (crescente/decrescente)
2 - K maiores ou menores por estoque
3 - Autocomplete por nome da peça
0 - Sair
```

Você pode escolher uma das opções para buscar, ordenar ou autocompletar nomes de peças.

---

## 📦 Dependências

✅ Nenhuma!  
Todo o projeto é feito com **bibliotecas padrão do Python**, como `json`.

---

## 🧠 Aprendizados Aplicados

- Algoritmos de ordenação (Merge Sort)
- Estrutura de dados: Heap e Árvore Binária
- Leitura e manipulação de dados JSON
- Projeto estruturado com separação de responsabilidades
- Execução via terminal interativo

---

## 📅 Desenvolvido para

**Challenge FIAP - Sprint 03  
Engenharia de Software**
