class Retangulo:
    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura

    def area(self):
        return self.l * self.a


# Para implementar a Retangulo não é necessário saber como funciona a classe por isso o código é Encapsulado
r = Retangulo(10, 5) # Só é preciso informar largura e altura

# Leva ao mal funcionamento pelo fato de não existir uma Interface Pública
r.l = 'teste'

print(r.area())