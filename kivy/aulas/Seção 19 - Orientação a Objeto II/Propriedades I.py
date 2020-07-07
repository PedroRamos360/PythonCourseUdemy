class A:
    def __int__(self):
        self._var = 0

    def _get_var(self):
        return self._var

    def _set_var(self, x):
        self._var = x

    var = property(fget=_get_var, fset=_set_var)


a = A()
a.var = 10
print(a.var)
# _var é a váriavel protegida
# var é a interface pública da classe