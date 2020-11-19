number= [1,2,3,4,5,6,7,8,9]

even = tuple(filter(lambda a: a%2 == 0,number))
print(even)

for i in even:
    print(i) 

    