# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
#Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#   [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя



a = [5, 2, 3, 4, 6, 1, 7]

for i in range(len(a)-2):
    if a[i]<a[i+1]>a[i+2] and a[i]<a[i+2]:
        a[i+1] = 0.1
    elif a[i]>a[i+1]<a[i+2] and a[i]<a[i+2]:
        a[i+1] = 0.1
    elif a[i]>a[i+1]<a[i+2] and a[i]>a[i+2]:
        a[i] = 0.1
    elif a[i]>a[i+1]>a[i+2] and a[i]>a[i+2]:
        a[i+1] = 0.1
        a[i+2] = 0.1

#a = list(filter(int, a))
b = [a[i] for i in range(len(a)) if type(a[i]) == int]

#print(a)
print(b)



