


def login_usuario(username, senha, arquivo='dados/usuarios.txt'):

    with open(arquivo, 'r') as a:
        linhas = a.readlines()

    for linha in linhas:
        username_existente , _ , senha_existente = linha.strip().split(';')

        if username == username_existente and senha == senha_existente:
            return True

    return False