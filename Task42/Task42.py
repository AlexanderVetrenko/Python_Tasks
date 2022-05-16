#Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#входные и выходные данные хранятся в отдельных текстовых файлах

def RLE_encode(tx):
    res = ''
    count = 1
    for i in range(len(tx)-1):
        if tx[i]!=tx[i+1]:
            res+=str(count) + tx[i]
            count = 1
        else: count+=1
    res+=str(count) + tx[len(tx)-1]
    return res

def RLE_decode(tx):
    res = ''
    count = ''
    for i in range(len(tx)-1):
        if tx[i].isdigit():
            count+=tx[i]
        else:
            res+=tx[i]*int(count)
            count = ''
    res+=tx[len(tx)-1]*int(count)
    return res

with open(r'E:\GeekEducation\Python\Python Tasks\Task42\Input.txt','r') as fl:
    dt = fl.read().split('\n')
    enc = dt[0]
    dec = dt[1]

with open(r'E:\GeekEducation\Python\Python Tasks\Task42\Output.txt','w') as fl1:
    fl1.write(RLE_encode(enc))
    fl1.write("\n")
    fl1.write(RLE_decode(dec))
