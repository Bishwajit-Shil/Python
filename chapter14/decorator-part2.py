def decorator_func(any_func):
    def wrapper(*args,**kwargs):
        print('awesome fohinni ra')
        return any_func(*args,**kwargs)
    return wrapper

@decorator_func
def func1(a):
    print(f'this is the first func : {a}')

func1(3)


@decorator_func
def func3(a,b):
    return a+b
print(func3(3,4))   



