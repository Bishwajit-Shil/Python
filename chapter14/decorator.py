def decorator_func(any_func):
    def wrapper():
        print('awesome fohinni ra')
        any_func()
    return wrapper

@decorator_func
def func1():
    print('this is the first func')

func1()
