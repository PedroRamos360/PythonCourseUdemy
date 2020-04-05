def maior(*params):
    maior = params[0]
    for number in range(len(params)):
        if params[number] > maior:
            maior = params[number]

    return maior


print(maior(2741, 242, 2, 42, 4, 4, 74, 2740))