#Задача 9. Вариант 24.

#Создайте игру,	в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
#Вслед за тем игрок должен попробовать отгадать слово.

#Cheraneva A.S.
#29.05.16

import random
WORDS=("клавиатура","мышь","наушники","компьютер","коврик","монитор")
word=random.choice(WORDS)
p=5
bukva=""
slovo=""
(chislo)=len(word)
print("Я выбрал слово, угадай какое. В этом слове ",str(chislo),"букв.")
print("У тебя " +str(p)+ " попытки угадать буквы")
while p>0:
	#print (word)
	bukva=input("Введите букву\n")
	if bukva in list(word):
		print("Да.")
		p=p-1
	else:
		print("Нет.")
		p=p-1
if p==0:
	slovo=input("Ваши попытки кончились. Угадайте слово")
	if slovo==word:
		print("Вы угадали слово")
	else:
		print("Вы не угадали слово")
input("Нажмите Enter для выхода.")