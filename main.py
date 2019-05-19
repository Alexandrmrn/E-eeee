import os
from os import walk

#Подключаем дополнительные модули для редактирования БД
#Создание и удаление базы данных
import method_db
#Редактирование базы данных
import edit_db

#Ввод пути для БД
ref = input("Please, write path for database \n")
ref = ref + '.db'
#Цикл обрабатывающий и вызывающий операции для рабоыт с БД
while True:
	if os.path.isdir(ref) == True:
		print('Path is directory')
	#Функция для создания БД
	if os.path.exists(ref) == False:
		print("Do you want to create database?  Y/N")
		ans = input()

		if ans == 'Y' or ans == 'y':
			#Вызов функции создания БД
			method_db.create_db(ref)

		elif ans == 'N' or ans == 'n':
			ans = input("Do you want to close programm? Y/N \n")

			if ans == 'Y' or ans == 'y':
				#Вызов функции завешения программы
				print('')
				quit()

			elif ans == 'N' or ans == 'n':
				continue

	elif os.path.exists(ref) == True:
		#Функция редактирования БД
		print("Do you want to edit database? Y/N")
		ans = input()

		if ans == 'Y' or ans == 'y':
			#Вызов функции редактирования баз данных
			edit_db.menu(ref)

		elif ans == 'N' or ans == 'n':
			ans = input("Do you want to close programm? Y/N \n")

			if ans == 'Y' or ans == 'y':
				exit()

			elif ans == 'N' or ans == 'n':
				continue
