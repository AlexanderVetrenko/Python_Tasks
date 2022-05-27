def Nov_Dta_UI():
    print('Создание новой записи справочника')
    f = 'д'
    b=[]
    while f == 'д':
        srnm = input('Фамилия: ')
        while srnm == "":
            srnm = input('Поле "Фамилия" должно быть заполнено: ')
        nm = input('Имя: ')
        tl = input('Телефон: ')
        while tl == "":
            tl = input('Поле "Телефон" должно быть заполнено: ')
        pr = input('Примечание: ')
        a=(srnm,nm,tl,pr)
        b.append(a)
        f=input('Желаете ввести еще данные? д/н ')
    return b