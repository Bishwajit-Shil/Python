# num = input('input one number(more digit) : ')

# total = 0
# for i in range(0,len(num)):
#     total += int(num[i])
# print(f'total : {total}')




name = input('Enter your name :')

char = ''
for i in range(0,len(name)):
    if name[i] not in char:
        char += name[i]
        print(f'{name[i]} : {name.count(name[i])}')
        