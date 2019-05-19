import os
import sqlite3

#Создание базы данных по определённому пути
def create_db(ref):
	st1=''
	#Подключение к БД(В данном случае создание файла с заданным именем в каталоге)
	conn = sqlite3.connect(ref)

	#Включение курсора
	c = conn.cursor() 

	# Создание таблицы
	name = input("Please, write Name of DB: ") 
	b = input("Please, write Names of colums DB through comma with space: ")
	b = b.split(',')
	#Цикл создания таблицыи создания столбцов
	i = 1
	st = name + '('
	for i in range(len(b)):
		st = st + b[i] 

	#создание БД
	st += ')'
	st = st.replace(' ', ',')
	print(st)
	c.execute('''create table '''+st+''' ''')
	#Сохранение данных
	conn.commit()


	#Сохранение (commit) изменений 
	conn.commit() 

	#Закрытие курсора 
	c.close()
	#Закрытие соединения
	conn.close() 