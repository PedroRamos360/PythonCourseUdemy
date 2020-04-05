def func(**params):
    return params


print(func(**dict(zip(('a', 'b', 'c'), (1, 2, 3)))))