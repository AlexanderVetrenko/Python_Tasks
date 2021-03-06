# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1


def Second_Encounter(ls, ind):
    count = 0
    k = 0
    for i in range(len(ls)):
        if ind == ls[i]:
           k+=1
           if k ==2: count = i
    return count if count !=0 else '-1'

ls1 = ["asd", "qwe", "zxc", "qwe", "ertqwe"]
ls2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
ls3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
ls4 = ["123", "234", 123, "567"]
ls5 = []
ind1 = "qwe"
ind2 = "йцу"
ind3 = "йцу"
ind4 = "123"
ind5 = "123"

print(f'Второе вхождение строки {ind1} в списке {ls1} равно {Second_Encounter(ls1, ind1)}')
print(f'Второе вхождение строки {ind2} в списке {ls2} равно {Second_Encounter(ls2, ind2)}')
print(f'Второе вхождение строки {ind3} в списке {ls3} равно {Second_Encounter(ls3, ind3)}')
print(f'Второе вхождение строки {ind4} в списке {ls4} равно {Second_Encounter(ls4, ind4)}')
print(f'Второе вхождение строки {ind5} в списке {ls5} равно {Second_Encounter(ls5, ind5)}')