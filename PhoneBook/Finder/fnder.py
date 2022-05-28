def fnd_srnm(srnm):
    #body = []
    res = []
    with open(r'E:\GeekEducation\Python\Python Tasks\PhoneBook\DataBase\Data.txt','r') as dt:
        body = dt.readlines()
        for line in body:
            if srnm in line:
                a = line.split(';')
                res.append(a[0])
    with open(r'E:\GeekEducation\Python\Python Tasks\PhoneBook\DataBase\Data.csv','r') as dt:
        a=''
        body = dt.readlines()
        for i in range(len(body)):
            if srnm in body[i]:
                a+=body[i].split('\n')[0]+' '+body[i+1].split('\n')[0]+' '+body[i+2].split('\n')[0]+' '+body[i+3].split('\n')[0]
                res.append(a)
                a=''

    return res


