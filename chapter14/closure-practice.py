def outer_func(x):
    def inner_func(n):
        return x**n
    return inner_func

var = outer_func(5)
print(var(2))

var2 = outer_func(9)
print(var2(2))
