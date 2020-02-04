def login():
    usuarioDigitado = input("Digite seu usuario: ")
    senhaDigitada = input("Digite sua senha: ")

    if (usuario == usuarioDigitado and senha == senhaDigitada):
        print("Bem vindo, {}".format(usuarioDigitado))
    else:
        print("Usuario ou senha incorreto, Tente Novamente")
        login()

usuario = input("Crie um usario: ")
senha = input("Crie uma senha: ")

login()
