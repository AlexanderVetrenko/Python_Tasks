# Найти сумму чисел списка стоящих на нечетной позиции

def Find_Odd_Sum(list):
    summ = 0
    for i in range(len(list)):
        if i%2 != 0:
            summ+=list[i]
    return summ

ls = [1,2,3,4,5,6,7,8,9]
print(f'Список {ls}')
print(f'Сумма чисел, стоящих на нечетной позиции, равна {Find_Odd_Sum(ls)}')