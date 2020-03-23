def login(usuario="root", senha="123"):
    print("Usuario: ", usuario)
    print("Senha: ", senha)


# Como a função tem parametros default não é necessário informá-los
login()
login(usuario="Cláudio")
login(senha="55691")
login(usuario="Cláudio", senha="55691")

