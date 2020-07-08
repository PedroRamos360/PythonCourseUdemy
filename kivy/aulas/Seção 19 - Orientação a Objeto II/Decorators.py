class A:
    def __int__(self):
        self._var = 0

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, x):
        self._var = x


a = A()
a.var = 10
t = a.var
print(t)

