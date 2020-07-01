class Retangulo:
    def __init__(self, largura, altura):
        self.altura = 0
        self.largura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A altura {} é inválida".format(num))
        self.altura = num

    def set_largura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A largura {} é inválida".format(num))

        self.largura = num

    def get_area(self):
        return self.altura * self.largura


r = Retangulo(largura=10, altura=20)
print(r.get_area())