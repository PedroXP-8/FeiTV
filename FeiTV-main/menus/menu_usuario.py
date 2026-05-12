import os
import time
import globals.session as session
from menus.menu_busca import menu_busca
from menus.menu_controle_favoritos import menu_controle_favoritos
from menus.menus_video import menu_timeline
from menus.menu_lista_favoritos import menu_favoritos


def menu_usuario():

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n' + '=' * 42)
        print('=' * 11 + " PÁGINA DO USUÁRIO  " + '=' * 11)
        print('=' * 42 + '\n')
        print(f"""Seja bem vindo {session.usuario_logado}!
O que deseja fazer?\n
1 --- ver algum vídeo
2 --- pesquisar por algum vídeo
3 --- ver lista de favoritos
4 --- criar/editar lista de favoritos
0 --- voltar para página inicial\n""")
        
        opcao = input('Digite umas das opções acima:  ').strip()
        if opcao == '1':
            menu_timeline()
        elif opcao == '2':
            menu_busca()
        elif opcao == '3':
            menu_favoritos()
        elif opcao == '4':
            menu_controle_favoritos()
        elif opcao == '0':
            break
        else:
            print('Opção inválida. Tente novamente.')
            time.sleep(2)