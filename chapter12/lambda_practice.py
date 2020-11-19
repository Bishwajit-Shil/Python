# even odd function
def even_odd(n):
    if n%2 == 0:
        return 'even'
  
    return 'odd'


    
# -----------------------------------------------
def even_odd(n):
    return n%2 ==0  


even = lambda a : a%2 == 0

print(even_odd(9))
print(even(10))


def last_char(s):
    return s[-1]
print(last_char('jitshil'))

l_char = lambda a: a[-1] 
print(l_char('jitshil'))   





# ----------------if else lambda----------------
def func(s):
    if len(s)>5:
        return True
    return False

print(func('abc'))

greater = lambda s :True if len(s)>5 else False
bigger = lambda s: len(s)>2
print(greater('abc'))
print(bigger('swarna roy popy'))