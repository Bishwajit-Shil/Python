# looking tuple
# tuple in one element
# tuple without parentthesis
#tuple unpacking
# list inside tuple
# tuple with some functions

mxied = (1,3,4,2,9.0)
for i in mxied:
    print(i)


# tuple one element
tu = (3,)
tu2 = ('string',)
print(type(tu))


# tuple unpacking
tu1,tu2,tu3,tu4,tu5 = (mxied)
print(tu1)



# tuple without parentthesis
tup = 'string', 'jitshil','programming',9
print(type(tup))


# list inside tuple
tuu = (3,5,[5,7,8,7])
tuu[2].pop()
print(tuu)


# functions 
print(sum(mxied))
print(min(mxied))
print(max(mxied))
