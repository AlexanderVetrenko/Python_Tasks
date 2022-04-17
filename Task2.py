#Найти максимальное из пяти чисел
def Find_Max(m,n,x,y,z):
    max = m
    if n>max:
        max = n
    if x>max:
        max = x
    if y>max:
        max = y
    if z>max:
        max = z
    return max

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
d = int(input('Введите четвертое число '))
e = int(input('Введите пятое число '))

print('Максимум равен ', Find_Max(a,b,c,d,e))