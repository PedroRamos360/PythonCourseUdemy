def palindromo(palavra):
    if palavra.lower() == palavra[::-1].lower():
        return True
    else:
        return False


print(palindromo(input()))
