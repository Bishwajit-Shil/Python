
# def function(name):
#     names = []
#     for i in name:
#         names.append(i[::-1])
#     return names


# def function(name):
#     return nam=[i[::-1] for i in name]
    

# nam = ['jitshil', 'swarna', 'nabila']    
# print(function(nam))    


# -----------------2nd process-------------------------

def function(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name[::-1].title() for name in l]

name= ['jit shil','sobro','roni']
print(function(name))     


