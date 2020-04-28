# Tratamentos de erro são compostos por try, except e/ou finally e/ou else
try:
    n = 10/int(input())
    print(n)
except ZeroDivisionError as error:
    print("Não é possível dividir por zero")
    print("Nome do erro:", error)
except (ValueError, NameError):
    print("Erro Desconhecido. Tipo do erro {}".format(NameError))
else:
    print("Programa finalizado com suceeso")
finally:
    print("Tenha um bom dia")
