class Retangulo:
    def __init__(self, largura, altura):
        self._altura = 0
        self._largura = 0
        self.altura = altura
        self.largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A altura {} é inválida".format(num))
        self._altura = num
        self.__var = 456

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A largura {} é inválida".format(num))

        self._largura = num

    @property
    def area(self):
        return self._altura * self._largura

    # altura = property(fget=_get_altura, fset=_set_altura)
    # largura = property(fget=_get_largura, fset=_set_largura)
    # area = property(fget=get_area)


r = Retangulo(largura=10, altura=20)
r.largura = 10
r.altura = 15
# r.area = 10 => gera erro porque "area" é uma propriedade readonly
print(r.altura, r.largura, r.area)