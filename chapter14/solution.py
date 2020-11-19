from functools import wraps
import time
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        anyt= any_func(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f'total time : {total_time}')
        return anyt
    return wrapper



@decorator_func
def func3(n):
    return [i**2 for i in range(1,n+1)]
func3(500)        
 



