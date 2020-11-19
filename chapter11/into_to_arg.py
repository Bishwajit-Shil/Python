#  make flexible function 

# * operator
# * args


def total(a,b):
    return a+b
print(total(4,5))


def all_total(*arg):
    return arg

print(all_total(2,3,4,5,5,6 ))    

