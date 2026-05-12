def cadastrar_usuario(username, email, senha, arquivo='dados/usuarios.txt'):

    if len(senha) < 6:
        return 'Senha inválida'
    
    with open(arquivo, 'r') as a:
        linhas = a.readlines()

    for linha in linhas:
        user_existente, email_existente, _ = linha.strip().split(';')

        if username == user_existente or email == email_existente:
            return 'erro de duplicidade'

    with open(arquivo, 'a') as a:
        a.write(f"\n{username};{email};{senha}")

    return 'cadastro concluído com sucesso'