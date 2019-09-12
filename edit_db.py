import sqlite3
import sys
#Вставка строки
def Inp(ref):
    conn = sqlite3.connect(ref)
    c = conn.cursor()
    NewStr = input('Введите значения от 1 до 9 через ;, которые вы хотите вставить в таблицу')
    NewStr = NewStr.split(';')
    c.execute("""INSERT INTO film VALUES ('""" + NewStr[0] +"""','""" + NewStr[1] +"""','""" + NewStr[2] +"""',
    '""" + NewStr[3] +"""','""" + NewStr[4] +"""','""" + NewStr[5] +"""',
    '""" + NewStr[6] +"""','""" + NewStr[6] +"""','""" + NewStr[8] +"""')""")
    conn.commit()
    c.close()
    conn.close()
#Вывод
def Output(ref):
    conn = sqlite3.connect(ref)
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM film")
        rows = c.fetchall()
        
        for row in rows:
            print(row)
    c.close()


#Функция замены
def Update(ref):
    conn = sqlite3.connect(ref)
    c = conn.cursor()
    Name = input('Введите названия фильма, куда вы хотите внести изменения: ')
    Zam = input('В каком столбце произвести замену: ')
    New = input('На что его заменить: ')
    c.execute("""UPDATE film SET """+Zam+"""= ? WHERE title= ? """, (New, Name,))
    conn.commit()
    print('Updating over')
    c.close() 
    conn.close()

#удаление строки
def Delet(ref):
    conn = sqlite3.connect(ref)
    c = conn.cursor()
    strok = input('Данные о каком фильме вы хотите удалить? ')
    c.execute("""DELETE FROM film WHERE title = ? """,(strok))
    conn.commit()
    print('Updating over')
    c.close()
    conn.close()
    Output(ref)


#выбор функции 
def menu(ref):
    while True:
        print('1 - Добавить строку\n2 - Изменить элементы в строке\n3 - Удалить строку по указанному критерию\n4 - Вывод таблицы\n5 - Выход')
        i = input('>>')
        if int(i) == 1:
            Inp(ref)
        if int(i) == 2:
            Update(ref)
        if int(i) == 3:
            Delet(ref) 
        if int(i) == 4:
            Output(ref)
        if int(i) == 5:
            quit()