import time
import os
import random
from load_videos.videos import carregar_videos, salvar_videos
from load_favoritos.favoritos import carregar_favoritos, salvar_favoritos
import globals.session as session

videos = carregar_videos()
favoritos = carregar_favoritos()

def menu_timeline():

    while True:

            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n' + '=' * 42)
            print('=' * 13 + " TIMELINE FEITV " + '=' * 13)
            print('=' * 42 + '\n')
                
            ids_escolhidos = random.sample(list(videos.keys()), 6)
            recomendados = [videos[i] for i in ids_escolhidos]

            print("Videos recomendados \n")
            for video in recomendados:
                    
                print(f"Título: {video['titulo']}")
                print(f"Duração: {video['duracao']}")
                print(f"Views: {video['views']}")
                print("-" * 30)
                    
            print('\nOpções de 1 a 6. \n7 para recarregar a página. \n0 para voltar.')
            opcaoV = input('\nEscolha algum Vídeo para assistir: ').strip()

            if opcaoV in ['1', '2', '3', '4', '5', '6']:
                indice = int(opcaoV) - 1
                menu_video(recomendados[indice])
            elif opcaoV == '7':
                print('\na página esta sendo recarregada.')
                time.sleep(4)
            elif opcaoV == '0':
                break
            else:
                print('opção inválida. Tente novamente.')
                time.sleep(4)

# MENU ASSISTINDO VIDEO

def menu_video(video):
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'{video['titulo']}')

        print('-' * 28)
        print('|' + ' ' * 26 + '|')
        print('|' + '  assistindo o vídeo....  ' + '|')
        print('|' + ' ' * 26 + '|')
        print('-' * 28)

        print("""\n1 -- curtir
2 -- descurtir
3 -- comentar
4 -- informações
5 -- adicionar em lista de favoritos
0 -- sair do vídeo""")

        opcao = input().strip()

        if opcao == '1':
            video['likes'] += 1
            print('você curtiu o vídeo.')
            salvar_videos(videos)
            time.sleep(2)

        elif opcao == '2':
            video['deslikes'] += 1
            print('você descurtiu o vídeo.')
            salvar_videos(videos)
            time.sleep(2)

        elif opcao == '3':
            comentario = input('\nDigite seu comentário: ')
            video['comentarios'].append(comentario)
            print('comentário adicionado.')
            salvar_videos(videos)
            time.sleep(2)

        elif opcao == '4':
            print(f"Título: {video['titulo']}")
            print(f"Duração: {video['duracao']}")
            print(f"Views: {video['views']}")
            print(f"Criador: {video['autor']}")
            print(f"Likes: {video['likes']}")
            print(f"Deslikes: {video['deslikes']}")
            print(f"Comentários: {video['comentarios']}")
            time.sleep(5)

        elif opcao == '5':
            menu_adicionar_video_favoritos(video)

        elif opcao == '0':
            break
        else:
            print('opção inválida. Tente novamente.')
            time.sleep(4)

# MENU ADICONAR VIDEOS AOS FAVORITOS

def menu_adicionar_video_favoritos(video):

    while True:

        playlists_usuario = {}

        for id_lista, lista in favoritos.items():
            if lista['dono'] == session.usuario_logado:
                playlists_usuario[id_lista] = lista

        if not playlists_usuario:
            print('\nVocê não possui playlists.')
            time.sleep(4)
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print('=' * 13 + " SUAS PLAYLISTS " + '=' * 13)
        print('=' * 42)

        ids_listas = list(playlists_usuario.keys())

        print('\n0 --- voltar')
        for i, id_lista in enumerate(ids_listas, start=1):
            lista = playlists_usuario[id_lista]
            print(f'{i} --- {lista["nome_lista"]}')
            print(f'Vídeos: {len(lista["videos"])}')

        escolha = input('\nEscolha uma playlist: ').strip()

        if escolha == '0':
            break 

        if escolha.isdigit():
            indice = int(escolha) - 1
            
            if 0 <= indice < len(ids_listas):
                id_playlist = ids_listas[indice]
                lista = playlists_usuario[id_playlist]

                video_id = None

                for id_v, dados_video in videos.items():
                    if dados_video == video:
                        video_id = id_v
                        break

                if video_id in lista['videos']:
                    print('\nEsse vídeo já está na playlist.')
                    time.sleep(4)

                else:
                    lista['videos'].append(video_id)
                    salvar_favoritos(favoritos)
                    print('\nVídeo adicionado à lista de favoritos.')
                    time.sleep(4)

            else:
                print('\nLista de favoritos inválida.')
                time.sleep(4)

        else:
            print('\nOpção inválida. Tente novamente.')
            time.sleep(4)
