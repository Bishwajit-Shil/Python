
# --------------------function palindom------------------
def _palindom(name):
    if name == name[::-1]:
         return True 
    return False    

nam = 'nan'
print(f'{_palindom(nam)}')   




