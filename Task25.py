# Написать программу преобразования десятичного числа в двоичное

def Dec_to_Bin(n):
    a =''
    ls = []
    while n!=0:
        ls.insert(0,n%2)
        n=n//2
    ls = list(map(str,ls))
    for item in ls:
        a = a+item
    return a
m = int(input('Введите целое число '))
print(f'Результат преобразования числа {m} в двоичное число равен {Dec_to_Bin(m)}')

