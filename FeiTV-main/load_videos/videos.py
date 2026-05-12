import json

def carregar_videos(arquivo='dados/videos.json'):
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return {int(k): v for k, v in dados.items()}

def salvar_videos(videos, arquivo='dados/videos.json'):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=4)