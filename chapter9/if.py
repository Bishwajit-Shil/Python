
# numbers = [1,2,3,4,5,6,7,8,9]

# num=[]
# for i in numbers:
#     if i%2 == 0:
#         num.append(i)
# print(num)        

# num1 = [i for i in numbers if i%2 == 0]
num2 = [i for i in range(1,11) if i%2 == 0]
# print(num1)
print(num2)

odd_num = [i for i in range(1,11) if i%2 != 0]
print(odd_num)