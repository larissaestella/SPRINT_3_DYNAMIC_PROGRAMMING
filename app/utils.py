import json

def carregar_dados(caminho="data.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
