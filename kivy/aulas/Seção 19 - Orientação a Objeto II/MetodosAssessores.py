class Retangulo:
    def __init__(self, largura, altura):
        # underline para restringir o uso das váriaveis
        self._altura = 0
        self._largura = 0

        # nome do atributo é desfigurado para evitar colisão de nomes
        self.__var = 0

        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A altura {} é inválida".format(num))
        self._altura = num
        self.__var = 456

    def set_largura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A largura {} é inválida".format(num))

        self._largura = num

    def get_area(self):
        return self._altura * self._largura


r = Retangulo(largura=10, altura=20)
print(r.get_area())