
def num_string(l):
    return [str(i) for i in l if type(i) == int]

l1 = [1,2,3,[3,4,5],'string'] 
print(num_string(l1))    

# def function(l):
#     lists = []
#     for i in l:
#         if type(i)== int:
#             lists.append(i)
#     return lists


# L = [1,[3,5,4],6,'string',9]
# print(function(L))

