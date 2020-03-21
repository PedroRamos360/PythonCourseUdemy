# Para verficar se uma váriavel está contido numa lista ou não
t = (1, 2, 3, 4, 5)
print(2 in t) # True
print(6 in t) # False
print(6 not in t) # True
print(1 in range(1, 6,)) # True
print(6 in range(1, 6,)) # False
x = range(1,6,)
if (3 in x):
    print("Contido")
else:
    print("Não contido")