import time
import os
from load_favoritos.favoritos import carregar_favoritos
from load_videos.videos import carregar_videos
from menus.menus_video import menu_video


videos = carregar_videos()
favoritos = carregar_favoritos()

def menu_favoritos():
 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print('=' * 15 + " PLAYLISTS  " + '=' * 15)
        print('=' * 42 + '\n')
        
        ids_favoritos = list(favoritos.keys())
        lista_favoritos = [favoritos[i] for i in ids_favoritos]
        for lista in lista_favoritos:
            if lista["visibilidade"] == "publica":
                print(f"\nNome da lista: {lista['nome_lista']}")
                print(f"Criador: {lista['dono']}")
                print("-" * 30)

        print(f"""\nEscolha alguma lista de favoritos para assistir:\n 
Opções entre 1 e {len(lista_favoritos)} 
0 --- voltar """)
        
        opcao = input("escolha alguma opção:  ").strip()
        if opcao.isdigit():
            indice1 = int(opcao) - 1 
            if 1 <= int(opcao) <= len(lista_favoritos):
            
                while True:

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""{lista_favoritos[indice1]['nome_lista']}
Criador : {lista_favoritos[indice1]['dono']}""")
            
                    for video_ids in lista_favoritos[indice1]['videos']:
                        video = videos[video_ids]
                        print(f"\nTítulo: {video['titulo']}")
                        print(f"Duração: {video['duracao']}")
                        print(f"Views: {video['views']}")
                        print("-" * 30)
                    
                    opcaoL = input(f"""\nDigite opções entre 1 e {len(lista_favoritos[indice1]['videos'])}
0 --- voltar\n""").strip()

                    if opcaoL == '0':
                        break
                    elif opcaoL.isdigit():
                        indice2 = int(opcaoL) - 1
                        if 1 <= int(opcaoL) <= len(lista_favoritos[indice1]['videos']): 
                            video_id = lista_favoritos[indice1]['videos'][indice2]
                            menu_video(videos[video_id])
                        elif opcaoL == '0':
                            break
                        else:
                            print('Opção inválida. Tente novamente')
                            time.sleep(4)
                    else:
                        print('Opção inválida. Tente novamente')
                        time.sleep(4)
                        
            elif opcao == '0':
                break
            else:
                print('Opção inválida. Tente novamente')
                time.sleep(4)
        else:
            print('Opção inválida. Tente novamente')
            time.sleep(4)