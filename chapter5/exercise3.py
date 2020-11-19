def reverse3(l):
    r_list = []
    for i in l:
        result = i[::-1]
        r_list.append(result)
    return r_list

s = ['abc','def','ghi']
print(reverse3(s))
