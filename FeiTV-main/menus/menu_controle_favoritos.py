import time
import os
from load_favoritos.favoritos import carregar_favoritos, salvar_favoritos
from load_videos.videos import carregar_videos
import globals.session as session

videos = carregar_videos()
favoritos = carregar_favoritos()


def menu_controle_favoritos():

    session.usuario_logado

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print(" MENU DE CONTROLE DE LISTAS DE FAVORITOS  ")
        print('=' * 42 + '\n')
        print("""1 --- Criar lista de favoritos
2 --- editar lista de favoritos
3 --- deletar lista de favoritos
0 --- voltar\n""")

        opcao = input("digite uma das opções: ")

        if opcao == '1':
            cirar_lista_favoritos()

        elif opcao == '2':
            editar_lista_favoritos()
        
        elif opcao == '3':
            deletar_lista_favoritos()
        elif opcao == '0':
            break
        else:
            print('Opção inválida. Tente novamente')
            time.sleep(4)

# MENU CRIAR LISTA DE FAVORITOS

def cirar_lista_favoritos():

    while True:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('=' * 42)
            print('=' * 5 + " CRIAÇÃO DE LISTAS DE FAVORITOS " + '=' * 5)
            print('=' * 42 + '\n')
            print('0 --- voltar')
            nome_lista = input('Digite o nome da sua nova lista de favoritos: ').strip()

            if nome_lista == '0':
                break

            ids_favoritos = list(favoritos.keys())
            lista_favoritos = [favoritos[i] for i in ids_favoritos]

            nome_existe = False

            for lista in lista_favoritos:
                if nome_lista.lower() == lista['nome_lista'].lower():
                    nome_existe = True
                    break

            if nome_existe:
                print('\nNome já existente. Tente outro.')
                time.sleep(4)

            else:
                novo_id = str(len(favoritos) + 1)

                favoritos[novo_id] = {
                    "nome_lista": nome_lista,
                    "dono": session.usuario_logado,
                    "likes": 0,
                    "visibilidade": "publica",
                    "videos": []}

                salvar_favoritos(favoritos)

                print('Nova lista de favoritos criada com sucesso!')
                time.sleep(4)
                break

# MENU EDITAR LISTA DE FAVORITOS

def editar_lista_favoritos():

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print('=' * 5 + " EDIÇÃO DE LISTAS DE FAVORITOS  " + '=' * 5)
        print('=' * 42 + '\n')
        print('0 --- voltar')
        edicao_nome_lista = input('digite o nome da lista para editar: ')

        if edicao_nome_lista == '0':
            break
    
        ids_favoritos = list(favoritos.keys())
        lista_favoritos = [favoritos[i] for i in ids_favoritos]

        lista_encontrada = None

        for lista in lista_favoritos:

            if edicao_nome_lista.lower() == lista['nome_lista'].lower():
                lista_encontrada = lista
                break
                
        if lista_encontrada is None:
            print('A lista de favoritos buscada não existe.')
            time.sleep(3)
            continue

        if lista_encontrada['dono'] != session.usuario_logado:
            print('\nVocê não pode editar essa playlist.')
            time.sleep(3)
            continue

               
        print(f"\nNome da lista: {lista['nome_lista']}")
        print(f"Criador: {lista['dono']}")
        print(f"Likes: {lista['likes']}")
        print(f"Vídeos: {lista['videos']}")
        print(f"Visibilidade: {lista['visibilidade']}")
        print("-" * 30)
        print("""\npossibilidades de edição:
1 --- Nome da lista de favoritos
2 --- excluir vídeos
3 --- alterar a visibilidade da Lista de favoritos
0 --- voltar""")

        edicao = input('\no que deseja editar?  ').strip()

        if edicao == '1':
            while True:
                print('0 --- voltar')
                novo_nome = input('digite o novo nome da lista de favoritos: ')
                if novo_nome == '0':
                    break
                lista_encontrada['nome_lista'] = novo_nome
                salvar_favoritos(favoritos)
                print('A alteração foi concluída.')
                time.sleep(4)
                break
                            
        elif edicao == '2':

            while True:

                if lista_encontrada['videos'] == []:
                    print('Sua lista de favoritos não tem vídeos.')
                    time.sleep(4)
                    continue

                for i, video_id in enumerate(lista_encontrada['videos'],start=1):
                    video = videos[video_id]
                    print(f"{i} --- {video['titulo']}")

                print('0 --- voltar')
                remover = input("Digite o número do vídeo para remover: ").strip()

                if remover == '0':
                    break

                if remover.isdigit():
                    indice_remover = int(remover) - 1

                    if 0 <= indice_remover < len(lista["videos"]):
                        lista_encontrada["videos"].pop(indice_remover)
                        salvar_favoritos(favoritos)
                        print("\nVídeo removido da playlist!")
                        time.sleep(4)
                        break

                    else:
                        print("\nVídeo inválido")
                        time.sleep(4)

                else:
                    print("\nOpção inválida. Tente novamente.")
                    time.sleep(4)

        elif edicao == '3':
            if lista['visibilidade'] == 'publica':
                lista['visibilidade'] = 'privada' 
                salvar_favoritos(favoritos)
                print('Visibilidade da lista de favoritos alterada para privada com suesso.')
                time.sleep(4)

            elif lista['visibilidade'] == 'privada':
                lista['visibilidade'] = 'publica' 
                salvar_favoritos(favoritos)
                print('Visibilidade da lista de favoritos alterada para publica com suesso.')
                time.sleep(4)
        elif edicao == '0':
            break

        else:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(4)


# MENU DELEÇÃO DE LISTA DE FAVORITOS 

def deletar_lista_favoritos():

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print('=' * 7 + " DELETAR LISTA DE FAVORITOS " + '=' * 7)
        print('=' * 42)
        print('\n0 --- voltar')
        nome_lista = input('Digite o nome da lista de favoritos: ').strip()

        if nome_lista== '0':
            break

        id_encontrado = None

        for id_lista, lista in favoritos.items():
            if nome_lista.lower() == lista['nome_lista'].lower():
                id_encontrado = id_lista
                break

        if id_encontrado is None:
            print('\nLista de favoritos não encontrada.')
            time.sleep(4)
            continue
            
        lista = favoritos[id_encontrado]

        if lista['dono'] != session.usuario_logado:
            print('\nVocê não pode excluir essa playlist.')
            time.sleep(4)
            continue
            
        confirmar = input(
            f'\nTem certeza que deseja excluir '
            f'"{lista["nome_lista"]}"? (s/n): '
        ).lower()

        if confirmar == 's':
            del favoritos[id_encontrado]
            salvar_favoritos(favoritos)
            print('\nList de favoritos excluída com sucesso!')
            time.sleep(4)

        else:
            print('\nExclusão cancelada.')
            time.sleep(2)