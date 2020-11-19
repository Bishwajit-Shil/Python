
# ----------------------reverse by revverse and l[::-1]
# def revers(l):
#     for i in l:
#         # l.reverse()
#         # return l
#         return l[::-1]
      

# s = [1,2,3,4]
# print(revers(s))



# ---------------------pop() and append(method)-------------------
def  _reverse_(l):
    r_list =[]
    for i in range(len(l)):
        pop = l.pop()
        r_list.append(pop)
    return r_list   
        


list1 = [1,2,3,4]  
print(_reverse_(list1))      