# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

#Первый способ - через множество, но здесь он выведет список элементов множества
#print('Введите последовательность целых чисел одной строкой. Разделитель - пробел')
#a = input()
#dt = a.split()
#dt = list(map(int, dt))
#dt = set(dt)
#dt = list(dt)
#print(dt)
#=======================================================================================
#Второй способ именно список тех элементов, у которых нет повторения

print('Введите последовательность целых чисел одной строкой. Разделитель - пробел')
a = input()
dt = a.split()
dt = list(map(int, dt))

unique = [i for i in dt if dt.count(i) == 1]
print(unique)