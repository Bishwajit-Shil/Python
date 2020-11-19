
user_info = {
    'name' : 'jitshil',
    'age' : 21,
    'fav_movie' : ['coco' , 'moco'],
    'fav_singer' : ['arijit','miner'],
}

# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')    

# if 'jitshil' in user_info.values():
#     print('present')
# else:
#     print('not present')    

# # ---------------------------------------------------------------------

# for i in user_info:
#     print(i)

# for i in user_info.values():
#     print(i)
    #   print(user_info[i])

# # ---------------------------------------------------------------------    
# # values method
# user_value = user_info.values()
# print(user_value)

# user_key = user_info.keys()
# print(user_key)


# ---------------------------------------------------------------

# # item methods
# for key,value in user_info.items():
#     print(f'key is : {key} and value is : {value}')

for i in user_info.items():
    print(i)    
