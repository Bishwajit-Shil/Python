# s ={1:1 , 2:4 , 3:9}

# dictionary = {num:num**2 for num  in range(1,11)}
# print(dictionary)

# dictionary2 = {f"key value is {num}" : num**2 for num in range(1,11)}
# print(dictionary)

string = 'jitshil'
count = {i:string.count(i) for i in string}
print(count)