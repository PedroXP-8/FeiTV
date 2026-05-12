import time
import os
from load_favoritos.favoritos import carregar_favoritos
from load_videos.videos import carregar_videos
from menus.menus_video import menu_video

videos = carregar_videos()
favoritos = carregar_favoritos()


def menu_busca():
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print('=' * 12 + " BUSCA POR VÍDEOS " + '=' * 12)
        print('=' * 42 + '\n')
        print('digite o nome do vídeo que deseja assistir: ')

        busca = input()

        videos_busca = []

        for video in videos.values():
            if busca in video['titulo'].lower():
                videos_busca.append(video)
            
        if videos_busca:
            for videoB in videos_busca:
                print(f"\nTítulo: {videoB['titulo']}")
                print(f"Duração: {videoB['duracao']}")
                print(f"Views: {videoB['views']}")
                print("-" * 30)
        
            print(f'\nOpções até {len(videos_busca)}.\n0 para voltar.')
            opcaoB = input('\nEscolha algum Vídeo para assistir: ').strip()

            if opcaoB.isdigit() and 1 <= int(opcaoB) <= len(videos_busca):
                    indice = int(opcaoB) - 1
                    menu_video(videos_busca[indice])
            elif opcaoB == '0':
                break
            else:
                print('opção inválida. Tente novamente.')
                time.sleep(4)

        else:
            print('\nNenhum vídeo foi encontrado.\nPesquise novamente ou volte para a página principal')
            print("\n0 --- voltar\nENTER para continuar busca")
            voltar = input()
            if voltar == '0':
                return