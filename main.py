"""Телефонный справочник"""

# param = значения требу  емых полей содержится в кортеже для исключения модификации и многократного использования.
param = ('Фамилия', 'Имя', 'Отчество', 'Название организации', 'телефон рабочий', 'телефон личный (сотовый)')


def record_output() -> None:
    """Постраничный вывод"""
    with open('file.txt', 'r', encoding="utf-8") as file:
        rfile = (file.read()).split('\n')
    fcount = len(rfile) - 1
    sti = 'Введите сколько записей выводить на странице? Целое число максимум ' + str(fcount) + ' :'
    num_of_entries = int(input(sti))
    j = 0
    page = 1
    r_num = 1
    for i in range(j, fcount, num_of_entries):
        print('Страница', page)
        page += 1
        con = i+num_of_entries
        con = min(con, fcount)
        for j in range(i, con):
            print(r_num, ', ', rfile[j])
            r_num += 1
        input()


def record_add() -> None:
    """Добавление новой записи в справочник

    :return:
    """
    with open('file.txt', 'r', encoding="utf-8") as file:
        # for line in file:   # Итерирует весь файл до конца, и берет последнюю строчку.
        #    pass
        line=tuple(enumerate(file))[-1][1]
        new_num = str(int(line.split(',')[0])+1)+','
        print()
    wstr = [new_num]
    for iter_param in enumerate(param):
        inp = input('Введите:'+iter_param[1])+','
        wstr.append(inp)
    wstr[-1] = wstr[-1][:-1]   # delete ','
    wstr.append('\n')
    print(wstr)
    with open('file.txt', 'a', encoding="utf-8") as file:
        file.writelines(wstr)
    # patronymic = input('Отчество :')
    # org = input('Организация :')
    # telw = input()
    # tell = input()


def modifi_record() -> None:
    """
    Редактирование записи.
    :return:
    """
    spr = []

    with open('file.txt', 'r', encoding="utf-8") as file:
        for line in file:
            app = line.strip().split(',')   # app.insert(0,str(rn))
            spr.append(app)  # список для последующей модификации
            # str(rn).ljust(5)+'  '+
            print(str(app))
    old_rec_num = int(input('Введите номер изменяемой записи:'))
    for iter_param in enumerate(param):
        print(int(iter_param[0])+1, iter_param[1])
    old_rec_par = int(input('Введите номер изменяемого параметра:'))
    new_rec = input('Введите значение изменяемого параметра:')
    spr[old_rec_num-1][old_rec_par] = new_rec
    with open('file.txt', 'w', encoding="utf-8") as file:
        for line in spr:
            linelen = len(line)
            for i in range(linelen-1):
                line[i] = line[i] + ','
            line[linelen-1] = line[linelen-1]+'\n'
            file.writelines(line)


def searching(obj: int, promt: str) -> list[int]:
    """ Функция поиска для всех полей. Поиск ведётся по полному совпалдению.
    :param obj:по какому полю ищем.
    :param promt: что ищем.
    :return: список порядковых номеров записей
    """

    cou_rec = 0
    search_rec = []
    with open('file.txt', 'r', encoding="utf-8") as file:
        for i in file:
            fil = i.split(',')
            fil[obj] = fil[obj].strip('\n')
            cou_rec += 1

        # print(fil[0],fil[ob])
            if fil[obj] == promt:
                search_rec.append(cou_rec)

    return search_rec


def record_search() -> None:
    """
    Поиск записи. Разделено на 2 функции основную и вспомогательную функцию "searching" предполагал использование
    в других частях программы например функция модификация.
    :return:
    """
    print('\nВыберете по каким параметрам будем искать и запишите их номера через пробел')
    for iter_param in enumerate(param):
        print(int(iter_param[0]) + 1, iter_param[1])
    par1 = input('Ввод :')
    # clear and sort list for "if"
    par1 = list(set(par1.split(' ')))
    par1.sort()
    print('Ищем в параметрах', par1)

    obr = ['', '1', '2', '3', '4', '5', '6']
    prefix = 'Содержится в строках:'
    for iter_par1 in enumerate(par1):
        print('par1=', iter_par1[1])
        print(param[int(iter_par1[1])-1])
        promt = input('Что ищем?')
        print(prefix, searching(int(iter_par1[1]), promt))

    if list(set(par1).difference(set(obr))):
        print("Не знаю такого параметра ", list(set(par1).difference(set(obr))))



if __name__ == '__main__':
    while True:
        print("Что желаете сделать?")
        print("1 Вывести весь справочник с заданием количества строк на странице")
        print("2 Добавить запись")
        print("3 Редактировать запись")
        print("4 Найти запись")
        print("5 Выйти")
        m = input("Введите номер пункта: ")
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
