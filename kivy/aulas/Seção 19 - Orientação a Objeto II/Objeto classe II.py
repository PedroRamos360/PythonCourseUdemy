# tudo declarado na classe será o corpo da classe (inclusive os métodos, diferentemente de C#)


class MinhaClasse:
    membro_cls = 50
    def __init__(self):
        self.membro_inst = -10 # membro de instância

    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)


i1 = MinhaClasse()
i2 = MinhaClasse()

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)

print('-'*30)

i1.membro_cls = 1000
print(MinhaClasse.membro_cls)
print(i1.membro_cls) # não acessa mais o valor da classe, acessa o valor da variável que foi declarada a ela
print(i2.membro_cls)

# i1.membro_inst = 10
# print('i1: {}'.format(i1.membro_inst))
# print('i2: {}'.format(i2.membro_inst))
#
# MinhaClasse.membro_cls = 9
#
# print('-'*20)
# print('i1: {}'.format(i1.membro_cls))
# print('i2: {}'.format(i2.membro_cls))
