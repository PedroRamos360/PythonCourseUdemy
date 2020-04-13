# import nome_do_modulo
import math

e1 = math.e
pi1 = math.pi

# Método mais eficiente:
import math as m

e2 = m.e
pi2 = m.pi

# Ou
from math import e, pi
e3 = e
pi3 = pi

print(e1, e2, e3, pi1, pi2, pi3)