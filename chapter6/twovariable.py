def two_variable(t1,t2):
    add = t1+t2
    multi = t1*t2
    return add, multi

# print(two_variable(3,4)) # we cann't use this
add,mult = two_variable(3,4)
print(add)
print(mult)