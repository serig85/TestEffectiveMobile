# param = значения требуемых полей содержится в кортеже для исключения модификации и многократного использования.
param = ('Фамилия', 'Имя', 'Отчество', 'Название организации', 'телефон рабочий', 'телефон личный (сотовый)')

def record_output():
    """Постраничный вывод"""
    f = open('file.txt', 'r')
    ro = (f.read()).split('\n')
    f.close()
    lro=len(ro)-1
    sti='Введите сколько записей выводить на странице? Целое число максимум '+str(lro)+' :'
    pc=int(input(sti))
    j=0
    page=1
    r_num=1
    for i in range(j,lro,pc):
        print('Страница',page)
        page += 1
        con=i+pc
        if con > lro:
            con = lro

        for j in range(i,con):
            print(r_num,', ',ro[j])
            r_num += 1
        input()

def record_add():
    """Добавление новой записи в справочник

    :return:
    """
    with open('file.txt') as f:
        for line in f:
            pass
        new_num = str(int(line.split(',')[0])+1)+','
    print()
    l=[new_num]
    f = open('file.txt', 'a')
    for p in range(len(param)):
        ip='Введите:'+param[p]
        inp = input(ip)+','
        l.append(inp)
    l[-1]=l[-1][:-1] # delete ','
    l.append('\n')
    print(l)
    f.writelines(l)
    # patronymic = input('Отчество :')
    # org = input('Организация :')
    # telw = input()
    # tell = input()
    f.close()


def modifi_record():
    """
    Редактирование записи.
    :return:
    """
    spr=[]
    rn=1


    with open('file.txt','r') as f:
        for line in f:
            app = line.strip().split(',')
            #app.insert(0,str(rn))
            spr.append(app) #список для последующей модификации
            s=str(app)
            #str(rn).ljust(5)+'  '+
            print(s)
            rn+=1


    #print(spr)

    old_rec_num=int(input('Введите номер изменяемой записи:'))
    for p in range(len(param)):
        print(p+1,param[p])
    old_rec_par=int(input('Введите номер изменяемого параметра:'))
    new_rec=input('Введите значение изменяемого параметра:')
    spr[old_rec_num-1][old_rec_par]=new_rec
    with (open('file.txt','w') as f):
        for line in spr:
            ll=len(line)
            for i in range(ll-1):
                line[i] = line[i] + ','
            line[ll-1]=line[ll-1]+'\n'
            f.writelines(line)


def searching(ob,promt):
    """ Функция поиска для всех полей. Поиск ведётся по полному совпалдению.
    :param ob:по какому полю ищем.
    :param promt: что ищем.
    :return: список порядковых номеров записей
    """

    cou_rec=0
    se=[]
    f = open('file.txt', 'r')
    for i in f:
        fil=i.split(',')
        fil[ob]=fil[ob].strip('\n')
        cou_rec +=1

        #print(fil[0],fil[ob])
        if fil[ob]==promt:
            se.append(cou_rec)
    f.close()
    return se


def record_search():
    """
    Поиск записи. Разделено на 2 функции основную и вспомогательную функцию "searching" предполагал использование
    в других частях программы например функция модификация.
    :return:
    """
    print('\nВыберете по каким параметрам будем искать и запишите их номера через пробел')
    for p in range(len(param)):
        print(p + 1, param[p])
    par1=input('Ввод :')
    # clear and sort list for "if"
    par1=list(set(par1.split(' ')))
    par1.sort()
    print(par1)

    obr=['','1','2','3','4','5','6']
    prefix='Содержится в строках:'
    for p in range(len(par1)):
        print('par1=',par1)
        print(param[int(par1[p])-1])
        promt=input('Что ищем')
        print(prefix,searching(int(par1[p]),promt))

    if list(set(par1).difference(set(obr))):
        print("Не знаю такого параметра ",list(set(par1).difference(set(obr))))







"""Коллектор функций"""
while True:
    print("Что желаете сделать?")
    print("1 Вывести весь справочник с заданием количества строк на странице")
    print("2 Добавить запись")
    print("3 Редактировать запись")
    print("4 Найти запись")
    print("5 Выйти")
    m=input("Введите номер пункта: ")
    match m:
        case '1':
            print("Вывести")
            record_output()
        case '2':
            print('Добавить')
            record_add()
        case '3':
            print('Редактировать')
            modifi_record()
        case '4':
            print('Найти')
            record_search()
        case '5':
            break

