l = [2,3,4,2,2,8,[66,77],[66]]
def list_count(l):
    count = 0
    for i in l:
        if type(i)== list:
            count += 1
    return count

print(list_count(l))