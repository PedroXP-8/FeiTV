import json

def carregar_favoritos():
    with open("dados/favoritos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    
def salvar_favoritos(favoritos):
    with open("dados/favoritos.json", "w", encoding="utf-8") as f:
        json.dump(favoritos, f, ensure_ascii=False, indent=4)

