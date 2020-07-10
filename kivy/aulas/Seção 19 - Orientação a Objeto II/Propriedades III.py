class Retangulo:
    def __init__(self, largura, altura):
        # underline para restringir o uso das váriaveis
        self._altura = 0
        self._largura = 0

        # nome do atributo é desfigurado para evitar colisão de nomes
        self.__var = 0

        self._set_altura(altura)
        self._set_largura(largura)

    def _get_altura(self):
        return self._altura

    def _set_altura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A altura {} é inválida".format(num))
        self._altura = num
        self.__var = 456

    def _get_largura(self):
        return self._largura

    def _set_largura(self, num):
        if not (isinstance(num, int) and num > 0):
            print('a')
            raise ValueError("A largura {} é inválida".format(num))

        self._largura = num

    def get_area(self):
        return self._altura * self._largura

    altura = property(fget=_get_altura, fset=_set_altura)
    largura = property(fget=_get_largura, fset=_set_largura)
    area = property(fget=get_area)


r = Retangulo(largura=10, altura=20)
r.largura = 10
r.altura = 15
print(r.altura, r.largura, r.area)