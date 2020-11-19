def outer_func():
    def inner_func():
        print('innter function')
    return inner_func

var = outer_func()
var()

def outer_func2(a):
    def inner_func2():
        print(f'there is {a}')
    return inner_func2

var3 = outer_func2('aweso;me')
var3()    