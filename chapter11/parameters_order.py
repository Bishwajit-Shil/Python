# PADK
# p--parameters
# A--*args
# D--default value
# K--**kwargs

def function(name, *args, last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

function('jitshil',1,2,3,a=1, b=2)   


