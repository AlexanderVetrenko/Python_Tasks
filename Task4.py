#Показать первую цифру дробной части числа 
a = input('Введите вещественное число ') #строковая 12.36

m = a.index('.')
print(a[m+1])