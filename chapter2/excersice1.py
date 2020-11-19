# ------------------------11111111-------------------------
num1, num2, num3= input('Enter three number  ').split()

print(f'{(int(num1) + int(num2) + int(num3))/3}')





# ----------------------------2222222222--------------------
name= input('what is your name: ')
print(name[-1::-1])





# -------------------------------333333333---------------------
name,char = input(r"what's your name & input a character in your name :").split(",")
print(f'lenght of your name  : {len(name)}')
# print(f'number of char :{name.lower().count(char.lower())}')
print(f'number of char{name.strip().lower().count(char.strip().lower())}')

 
