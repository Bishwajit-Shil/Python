# without enumerate function
names=['jit','abc','ru']
# pos=0
# for name in names:
#     print(f'{pos}----->{name}')
#     pos +=1


    # with enumerate function

# for pos, name in enumerate(names):
#     print(f'{pos}--------->{name}') 

def postion(l,target):
    for pos ,name in enumerate(l):
        if name == target:
            return pos
    return -1   

print(postion(names,'jit'))     