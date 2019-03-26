import sys
import os


def exit():
    m = input('Вы хотите продолжить? (y/n)')
    if m == 'y':
        menu()
    else:
        sys.exit()


def count_files():
    DIR = 'C:\\Users\\Admin\\Desktop\\py'
    print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    exit()


def show_products():
    k = 0
    file = open(b'C:\\Users\\Admin\\Desktop\\py\\file.txt', 'r', encoding='UTF-8')
    n_list = file.read().splitlines()
    for elem in n_list:
        n_list[k] = elem.split(';')
        k += 1
    header = n_list.pop(0)
    print('%3s%20s%10s%10s' % (header[0], header[1], header[2], header[3]))
    n_list.sort(key=lambda x: x[1])
    for elem in n_list:

        if int(elem[2]) > 1700:
            print('%3s%20s%10s%10s' % (elem[0], elem[1], elem[2], elem[3]))
    exit()


def change_cost():
    k = 0
    file = open(b'C:\\Users\\Admin\\Desktop\\py\\file.txt', 'r', encoding='UTF-8')
    n_list = file.read().splitlines()
    for elem in n_list:
        n_list[k] = elem.split(';')
        k += 1
    header = n_list.pop(0);
    print('%3s%20s%10s%10s' % (header[0], header[1], header[2], header[3]))
    n_list.sort(key=lambda x: x[1])
    for elem in n_list:
        print('%3s%20s%10s%10s' % (elem[0], elem[1], elem[2], elem[3]))
    print('Введите номер товара, стоимость которого хотите изменить:')
    num = input('>>')
    print('Введите на сколько уменьшить:')
    cost = input('>>')
    for elem in n_list:
        if elem[0] == num:
            print('Товар: {}'.format(elem))
            elem[2] = int(elem[2]) - int(cost)
            print('Измененный товар: {}'.format(elem))
            if int(elem[2]) == 0:
                print('Уверены, что хотите отдать товар даром?')
            if int(elem[2]) < 0:
                print('Хотите доплатить за покупку товара?')
    i = input('Сохранить измененный список товаров в файл? (y/n)')
    if i == 'y':
        f = open(b'C:\\Users\\Admin\\Desktop\\py\\file.txt',  'w', encoding='UTF-8')
        f.write(str(header) + '\n')
        for elem in n_list:
            f.write(str(elem) + '\n')
        print('Файл записан!')
        exit()
    else:
        exit()

def menu():
    print('0 - Выход\n1 - Посчитать файлы в директории\n2 - Вывод информации о товарах, сортированных по значению'
          '\n3 - Изменение количества товаров указанных номеров')
    m = input('>>')
    if m == '0':
        sys.exit()
    if m == '1':
        count_files()
    if m == '2':
        show_products()
    if m == '3':
        change_cost()


menu()