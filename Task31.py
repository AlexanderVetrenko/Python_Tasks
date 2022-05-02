# Составить список простых множителей натурального числа N

def Simpl_Mult(n,ls = []):
    if n == 1:
        return ls
    else:
        for k in range(2, n+1):
            if n%k == 0: 
                ls.append(k)
                break
        n//=k
        return Simpl_Mult(n,ls)

print('Введите натуральное число N')
a = int(input())
print(f'Список простых множителей числа {a} равен {Simpl_Mult(a)}')