def func(a):
    return a**2

l=[1,3,4,6]
print(list(map(func,l)))    

# we can make a function as like map-function
def my_map(function,l):
    new_list = []
    for item in l:
        new_list.append(function(item))
    return new_list

print(my_map(func,l))

print(my_map(lambda a:a**3 , l))