# argument with normal parameter

def multiple_nums(num ,*args):
    multi =1 
    print(num)
    for i in args:
        multi *= i
    return multi


print(multiple_nums(1,2,3,5,6,7))


