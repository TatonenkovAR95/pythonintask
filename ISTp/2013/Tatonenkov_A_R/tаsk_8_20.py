# Задача 8. Вариант 20.
# Доработайте игру Анаграммы так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
import random
words = ("хоккей","табло","игрок","ворота","гол","клюшка")
word = random.choice(words)
correct = word
jumble = ""
hint = ""
ball = 100

while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]
	
print (
"""
Добро пожаловать в игру 'Анаграмма'
Надо переставить буквы так, чтобы получалось осмысленное слово.
(Для выхода нажмите Enter, не вводя версии.)
"""
)

print ("Вот анаграмма:", jumble)
guess = " "
while guess != correct and guess != "":
	guess = input("Попробуйте отгадать исходное слово: ")
	if guess == "подсказка":
		hint = (correct[:position+1])
		print (hint)
		ball -= 10
		position += 1	
	elif guess == correct:
		print ("Вы отгадали!\n")
		print ("Ваши баллы", ball)
	elif guess != correct:
		print ("Неправильно, попробуйте еще раз.")
		
print ("Спасибо за игру.")

input("\n\nНажмите Enter для выхода.")

# 21.12.2016
# Tatonenkov A.R.
