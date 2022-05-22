from random import randint
import Chck

def player_player(cn,mx):
    pl1 = input('Введите имя первого игрока ')
    pl2 = input('Введите имя второго игрока ')

    if randint(1,2) == 1: 
        print(f'Игру начинает {pl1}')
        f = 1
    else:
        print(f'Игру начинает {pl2}')
        f = 2
    
    while cn>mx:
        if f==1:
            n = int(input(f'Ход {pl1} '))
            n = Chck.check_nmbr(n,mx)
            cn-=n
            print(f'Монет осталось: {cn}')
            f=2
        else:
            n = int(input(f'Ход {pl2} '))
            n = Chck.check_nmbr(n,mx)
            cn-=n
            print(f'Монет осталось: {cn}')
            f=1

    if f == 1: print(f'Победил {pl1}')
    else: print(f'Победил {pl2}')