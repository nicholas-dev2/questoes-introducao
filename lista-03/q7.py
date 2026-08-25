usuário, senha = "Nicholas", "12345"

while True:
    autenticação = input("Insira o nome de usuário: ")

    if autenticação.strip() == usuário:
        pass
    else:
        print("Credenciais inválidas. Acesso bloqueado!")
        break

    autenticação = input("Insira sua senha: ")

    if autenticação.strip() == senha:
        print("Acesso liberado. Bem-vindo ao SUAP!")
        break
    else:
        print("Credenciais inválidas. Acesso bloqueado!")
        break