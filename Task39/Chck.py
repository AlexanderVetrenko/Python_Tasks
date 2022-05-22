def check_nmbr(s,z):
    if s in range(1,z+1): 
        return s
    else:
        while s not in range(1,z+1):
            print('Укажите правильное количество монет!')
            s = int(input())
        return s