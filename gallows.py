import urllib.request
import os

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def main_menu () :
	play=1
	while play>0:
		print("""Добро пожаловать в игру ""Виселица""!\n    Пожалуйста, выберите нужный пункт меню:
		1) Новая игра
		2) Настройки
		3) Выход""","\n ")
	mode=input("Ваш выбор: ")
	if mode=="1":
	    import viselica
	elif mode=="2":
	    print("Меню настроек:\n#пока находится в тестовом режиме#\n ")
	else:
	    play=0
	    print("Спасибо что зашли на огонек! Досвидания")

def drow_word (secret_word, user_letters ):
	word_to_drow = []
	for letter in secret_word :
		if letter in user_letters :
			word_to_drow.append(letter)
		else :
			word_to_drow.append("_")
	return ''.join(word_to_drow)

def main():
	slovo = urllib.request.urlopen("http://www.setgetgo.com/randomword/get.php?q=4").read().decode("utf-8").lower()
	print(slovo)
	t=7
	m=1
	i=0
	let=''
	space=(' ')
	print (drow_word(slovo, let))
	while t>0:
		print('\nу вас ',t,' попыток')    
		let1=input('введите букву: ')
		if slovo.find(let1)!=-1 and len(let1)==1 and let1.isdigit()==False and let.find(let1)==-1:
			cls()
			print(drow_word(slovo, let + let1))
		elif let1.isdigit()==True or len(let1)!=1:
			print("Мы играем в слова! Попробуйте ввести одну букву снова.")
		elif let.find(let1)>-1:
			print('Вы уже выбирали эту букву. Попробуйте другую.')
		else:
			t-=1
			print('НЕ УГАДАЛ!! Попытайся еще!')
		let=let + let1
		if set(let).intersection(set(slovo)) == set(slovo):
			print("Поздравляем! Вы выиграли, и на этот раз виселится останется без работы =(")
			break
	else:
		print("Вы проиграли!")
		print("Ответ был: ",slovo,'\n')
	ch=input("Хотели бы вы сыграть еще раз?(Y/N)")
	while m!=0:
		if ch.lower()=="y":
			m-=1
		elif ch.lower()=="n":
			break
		else:
			print("Y или N... других ответов НЕТ!") 

if __name__ == "__main__":
	main()