number1=[2,4,6,8,10]
number2 = [1,2,3,5,66]

# even = []
# for  num in number1:
#     even.append(num%2 ==0)
# print(even)    

print(all(num%2 == 0 for num in number1))
print(any(i%2 == 0 for i in number2))
