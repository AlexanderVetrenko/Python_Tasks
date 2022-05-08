# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.

from random import randint

def Empty_Mmbr(s):
    n = int(s.split('x')[0])
    if n!= 0: return True
    else: return False

print('Введите натуральную степень k многочлена')
a = int(input())

ls = []
for i in range(a+1):
    ls.append(randint(0,2))
ls = list(map(str,ls)) 

n = a
for i in range(a+1):
    if n > 1:
        ls[i] = ls[i] + 'x**'+str(n)
    elif n == 1:
        ls[i] = ls[i] + 'x'
    n-=1
    if n == 0: break

ls = list(filter(Empty_Mmbr,ls))

st = ''

for i in range(len(ls)):
    if i != len(ls)-1:
        st = st+ls[i]+ ' + '
    else:
        st = st+ls[i]+ ' = 0 '
  
with open(r'E:\GeekEducation\Python\Python Tasks\Task33\File.txt','a') as dt:
    dt.write(st+'\n')



