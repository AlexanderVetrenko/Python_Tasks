#Дано число. Проверить кратно ли оно (5 и 10) или 15, но не 30

a = int(input('Введите целое число '))

if (a%5 == 0 and a%10 == 0) and a%30!=0:
    if (a%15 == 0 and a%30!=0):
        print('Число соответствует условию задачи')
    else: print('Число не соответствует условию задачи')
else: print('Число не соответствует условию задачи')