from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper(*args,**kwargs):
        '''this is decorator '''
        print('awesome fohinni ra')
        return any_func(*args,**kwargs)
    return wrapper



@decorator_func
def func3(a,b):
    '''this is func'''
    return a+b   
print(func3.__doc__)
print(func3.__name__)



