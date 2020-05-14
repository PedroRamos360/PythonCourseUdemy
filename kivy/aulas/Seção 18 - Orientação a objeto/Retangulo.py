class Retangulo:
    def __init__(self):
        self.a = 0
        self.b = 0

    def area(self):
        return self.a * self.b


r1 = Retangulo()
r1.a = 10
r1.b = 5
print(r1.area())