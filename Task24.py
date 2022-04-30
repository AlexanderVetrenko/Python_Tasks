# В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной 
# части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def List_Clean(a:str):
    f= False
    for i in range(len(a)):
        if a[i] == '.': f = True
    return True if f == True else False

def Drohb(a:str):
    b = a.split('.')
    return round((float(a) - int(b[0])), 2)

def MiniMaks(ls):
    min = ls[0]
    max = ls[0]
    for item in ls:
        if item > max: max = item
        if item < min: min = item
    return (max-min)

a = input('Введите строку вещественных чисел. В качестве разделителя используйте пробел ')
dt = list(filter(List_Clean,a.split()))
dt = list(map(Drohb, dt))

print(f'Разница между максимальным и минимальным значениями дробной части элементов равна {MiniMaks(dt)}')

