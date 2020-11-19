user_info = {
    'name' : 'jitshil',
    'age' : 21,
    'fav_movie' : ['coco' , 'moco'],
    'fav_singer' : ['arijit','miner'],
}

# ----------------------------------------------------------------
# d = dict.fromkeys(['name','age'], 'pagla')
# # d = dict.fromkeys(range(1,11),'unknown')
# print(d)

# ----------------------------------------------------------
# print(user_info['name'])
# print(user_info.get('name')) #that's better


# -----------------------------------------------------------------

# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')    

# if user_info.get('name'):
#     print('present')
# else:
#     print('not present')



# ------------------------------------------------------------

d = user_info.copy()
print(d)


user_info.clear()
print(user_info)