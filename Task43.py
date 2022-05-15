# Напишите программу, удаляющую из текста все слова содержащие "абв".

def Del_Word(s):
    f = True
    for i in range(len(s)-2):
        if (s[i]+s[i+1]+s[i+2]) == 'абв':
            f =  False
    return f


print('Введите текст ')
a = input()

a = a.split()
print(a)
a = list(filter(Del_Word,a))
print(a)


