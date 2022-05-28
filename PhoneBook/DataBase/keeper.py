def Sav_Dt(matr, f):
    if f == 1:
        with open(r'E:\GeekEducation\Python\Python Tasks\PhoneBook\DataBase\Data.txt','w') as dt:
            for i in range(len(matr)):
                for item in matr[i]:
                    dt.write(item)
                    dt.write(' ')
                dt.write(';')
                dt.write('\n')
    elif f == 2:
        with open(r'E:\GeekEducation\Python\Python Tasks\PhoneBook\DataBase\Data.csv','w') as dt:
            for i in range(len(matr)):
                for item in matr[i]:
                    dt.write(item)
                    dt.write('\n')
                dt.write(' ')
                dt.write('\n')