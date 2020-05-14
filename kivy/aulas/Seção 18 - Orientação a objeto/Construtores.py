# Construtor é um método que é executado toda vez que a classe é inicializada

class A:
    # Criação de construtor:
    def __init__(self):
        print(id(self))


a = A()
print(id(a))