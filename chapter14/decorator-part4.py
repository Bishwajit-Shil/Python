from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper(*args,**kwargs):
        '''this is decorator '''
        print(f'{any_func.__name__}')
        print(f'{any_func.__doc__}')
        print('awesome fohinni ra')
        return any_func(*args,**kwargs)
    return wrapper



@decorator_func
def func3(a,b):
    '''this is func'''
    return a+b   
func3(4,6)    




