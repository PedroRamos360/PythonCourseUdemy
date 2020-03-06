# iterando listas em python
lista_nums = [100, 200, 300, 400]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000

print(lista_nums)

# ou
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000

print(lista_nums)