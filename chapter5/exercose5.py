
def common_list(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output        



list1 = [3,4,5,2]
list2 = [3,6,7,2]
print(common_list(list1,list2))
