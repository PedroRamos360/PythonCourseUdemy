class Pessoa:
    a = 1


# Objetos:
p1 = Pessoa()
p2 = Pessoa()

p1.a += 10
p2.a -= 10

# p2.a não tem relação com p1.a já que são objetos diferentes
print(p2.a, p1.a)

