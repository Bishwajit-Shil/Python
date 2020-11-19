def function(**args):
    for k,v in args.items():
        print(f'{k} :{v}')


# function(first_name='Jit' , last_name='Shil')

d = {  'name':'jitshil',' age':24 }
function(**d)



