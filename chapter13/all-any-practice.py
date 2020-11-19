def my_sum(*args):
    if all([(type(args)==int or type(args)== float) for arg in args]):
        total=0
        for num in args:
            total += num
        return total
    return 'wrong input'    

l = (1,2,3,4,5,6,7.8,'jitshil',['hello'])
print(my_sum(l))    


