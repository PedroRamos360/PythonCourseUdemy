class Retangulo:
    def area(self):
        return self.a * self.l

# declaração de membros
def membros_retangulo(r):
    r.a = 0
    r.l = 0


r1 = Retangulo()
membros_retangulo(r1)
r1.a = 10
r1.l = 5

print(r1.area())