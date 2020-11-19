# def function(a):
#     list1 = []
#     for i in a:
#         list1.append(i**2)
#     return list1


numbers=[1,2,3,4]
# print(function(numbers))  
# ------------------------------------------------------------
# def squar(a):
#     return a**2
# square = list(map(squar, numbers))
# print(square)

square2 = list(map(lambda a: a**2, numbers ))
print(square2)

# -------------------------------------------------------------------
name =['jit', 'sobro', 'sami']
count = list(map(len, name))
print(count)
