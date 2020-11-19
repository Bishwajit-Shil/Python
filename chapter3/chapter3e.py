# ----------------------first-------------------
winning_num= 10
guess_num= int(input('Enter two number for win :  '))

if(guess_num==winning_num):
    print('You win')
elif(guess_num>winning_num):
    print('TOO high')
else:
    print('TOO low')    
 





# -----------------------second----------------
u_name= input('Enter your name :  ')
u_age= int(input('Enter yout age : '))


if (u_name[0] == 'j' or u_name[0] == 'J') and u_age > 10:
    print('You can watch')
else:
    print('You are not elligible')







# -------------------------third---------------------
num= int(input('enter any number : '))
total = 0
i = 1
while i<= num:
    total= total+i
    i= i+1
print(f'the calculated total for {num} , {total}')     







# ---------------------------4th---------------------------------
num = input('Enter more than one number : ')

# total = 0
# i = int(num[0])
# while i<= int(num[-1]):
#         total  += i
#         i += 1
# print(f'total sum is {total}')  

total = 0
i = 0
while i<= len(num):   
        total = total + i
        i = i + 1
print(f'total sum {total}')        




# --------------------------5th-----------------------
name =input('enter your name :')

var_temp = ""
i = 0
while i <= len(name):
    if name[i] not in var_temp:
        var_temp += name[i]
        print(f'{name[i]} : {name.count(name[i])}')
    i += 1



