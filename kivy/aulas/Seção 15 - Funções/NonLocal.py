var_local = 0


def func_non_local():
    var_local = 10

    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()


func_non_local()
