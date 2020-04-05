# Váriaveis acessáveis de qualquer lugar do código

a = 1
b = 2
c = 3


def func():
    x = 10
    print(x)
    print(locals())  # Mostra as váriaveis locais


func()
print(globals()) # Mostra todas as váriaveis globais
# não retorna x porque este não é global


def func_global():
    global a # para acessar uma váriavel do escopo global
    a = 10
    print(a)


func_global()
print(a)




