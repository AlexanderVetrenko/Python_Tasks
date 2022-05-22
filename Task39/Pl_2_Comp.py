from random import randint
import Chck

def player_comp(cn,mx):
    pl = input('Введите имя игрока ')
    
    if randint(1,2) == 1: 
        print(f'Игру начинает {pl}')
        f = 1
    else:
        print(f'Игру начинает компьютер по имени "Доктор Зло"')
        f = 2
    
    while cn>mx:
        if f==1:
            if cn%(mx+1) == 0: teg=1 
            else: teg = cn%(mx+1) 
            n = int(input(f'Ход {pl}, подсказка {teg} '))
            n = Chck.check_nmbr(n,mx)
            cn-=n
            print(f'Монет осталось: {cn}')
            f=2
        else:
            if (cn%(mx+1)) == 0: n = 1
            else: n = cn%(mx+1)
            print('Ход Доктора Зло ', n)
            cn-=n
            print(f'Монет осталось: {cn}')
            f=1

    if f == 1: print(f'Победил {pl}!')
    else: print(f'Победил Доктор Зло!')