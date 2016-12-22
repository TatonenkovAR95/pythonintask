# Задача 10. Вариант 20.
#


print ("""
			Добро пожаловать в "Генератор персонажей". 
		Вы можете распределить 30 очков между 4 характеристиками:
	Сила, Здоровье, Мудрость и Ловкость. Вы можете как и брать из общего
числа пункотв, так и возвращать. Распределяйте характеристики с умом. Удачи!
	""")


STR = 0
HP = 0
INT = 0
AGL = 0
point = 30
chislo = 0

print ("Если хотите изменить Силу, то напишите 'Сила'. Если Здоровье, то 'Здоровье'. Если  Мудрость, то 'Мудрость'. Если Ловкость, то 'Ловкость'.")


while True:
	if STR < 0 or HP < 0 or INT < 0 or AGL < 0 or point> 30:
		print ("Ошибка")
		break
		
	elif point == 0:
		print ("Вы распределили очки: \nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL)
		break
		
	print ("Ваши очки: \nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL, "\nНераспределённые очки:",point)
	user_input = input("")
	
	if user_input == "Сила":
		chislo = int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point:
			STR += chislo
			point -= chislo
			
		else:
			print('Перебор')
			
	elif user_input == "Здоровье":
		chislo = int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point:
			HP += chislo
			point -= chislo
			
		else:
			print('Перебор')
			
	elif user_input == "Мудрость":
		chislo = int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point:
			INT += chislo
			point -= chislo
			
		else:
			print('Перебор')
			
	elif user_input == "Ловкость":
		chislo = int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point:
			AGL += chislo
			point -= chislo
			
		else:
			print('Перебор')
			
input("\n\nНажмите Enter для выхода.")

# 21.12.2016
# Tatonenkov A.R.
