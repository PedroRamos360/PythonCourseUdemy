def programa():
    mes = int(input())
    if mes > 12 or mes < 1:
        print("Entrada Incorreta. Tente Novamente")
        programa()
        return

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    print(meses[mes - 1])

programa()