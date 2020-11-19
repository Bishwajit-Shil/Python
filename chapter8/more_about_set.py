
s = {1,3,4,5,'string'}

if 'string' in s:
    print('y')
else:
    print('N')


for item in s:
    print(item)


s1 = {2,3,4,6}
s2 = {2,4,2,6}

#union kora jai by pipe using
inter = s1 & s2
print(inter)



