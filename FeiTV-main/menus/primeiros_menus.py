import time
import os
import sys
from controle_acesso.controle_cadastro import cadastrar_usuario
from controle_acesso.controle_login import login_usuario
from menus.menu_usuario import menu_usuario
import globals.session as session

def primeiro_menu():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 42)
        print('=' * 16 + "  FEI TV  " + '=' * 16)
        print('=' * 42 + '\n')
        print("""1 --- login
2 --- cadastro
0 --- sair\n""")
        
        opcao = input('digite umas das opções acima:  ').strip()

        if opcao == '1':
            menu_login()
        elif opcao == '2':
            menu_cadastro()
        elif opcao == '0':
            print('\nObrigado pela visita em nosso site!!')
            sys.exit()
        else:
            print('Opção inválida. Tente novamente.')
            time.sleep(1.5)

def menu_login():

    while True: 
            os.system('cls' if os.name == 'nt' else 'clear')    
            print('\n' + '=' * 42)
            print('=' * 12 + " PÁGINA DE LOGIN  " + '=' * 12)
            print('=' * 42 + '\n')
                
            usernameL = input('digite seu nome de usuario: ').strip()
            senhaL = input('digite a sua senha: ').strip()

            if login_usuario(usernameL, senhaL):
                session.usuario_logado = usernameL
                menu_usuario()
                break
                    
            else:
                print('\nlogin inválido. Tente novamente.')
                print("\n0 --- voltar\nENTER para continuar login")
                voltar = input()

                if voltar == '0':
                    break

# MENU CADASTRO

def menu_cadastro():

    while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n' + '=' * 42)
            print('=' * 11 + " PÁGINA DE CADASTRO " + '=' * 11)
            print('=' * 42 + '\n')
                
            usernameL = input('digite seu nome de usuario: ').strip()
            emailL = input('digite seu email: ').strip()
            senhaL = input('digite a sua senha: ').strip()

            resultado = cadastrar_usuario(usernameL,emailL, senhaL)

            if resultado == 'Senha inválida':
                print('Sua senha precisa ter mais de 6 caracteres,')
                time.sleep(4)
            elif resultado == 'erro de duplicidade':
                print('Nome de usuário ou email ja existentes.')
                time.sleep(4)
            else:
                print("\nCadastro realizado com sucesso!\nFaça agora o login na plataforma!")
                time.sleep(4)
                break
                
            print('\nlogin inválido. Tente novamente.')
            print("\n0 --- voltar\nENTER para continuar login")
            voltar = input()
            if voltar == '0':
                break