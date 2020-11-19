def multiple_nums(*args):
    multi =1 
    print(*args)
    for i in args:
        multi *= i
    return multi

num = [3,34,5,3]
print(multiple_nums(*num))    

