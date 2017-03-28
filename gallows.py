import urllib.request
import os

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def drow_word ( letters ):
	#print("we are in function drow")
	#print (letters)
	#print (slovo)
	word_to_drow = []
	for letter in slovo :
		if letter in letters :
			word_to_drow.append(letter)
		else :
			word_to_drow.append("_")
	#print (word_to_drow)
	#print("end of function drow")
	return ''.join(word_to_drow)


slovo=urllib.request.urlopen(
        "http://www.setgetgo.com/randomword/get.php/requestStr").read().decode("utf-8").lower()
x1=list(slovo)
# print(slovo, x1)
t=7
m=1
i=0
let=''
space=(' ')
answ="_"*len(x1)
preansw=space.join(list(answ))
#print(preansw)
print (drow_word(let))
while t>0:
    print('\nу вас ',t,' попыток')    
    let1=input('введите букву: ')
    if slovo.find(let1)!=-1 and len(let1)==1 and let1.isdigit()==False and let.find(let1)==-1:
        cls()
        print(drow_word(let + let1))
    elif let1.isdigit()==True or len(let1)!=1:
        print("Мы играем в слова! Попробуйте ввести одну букву снова.")
    elif let.find(let1)>-1:
        print('Вы уже выбирали эту букву. Попробуйте другую.')
    else:
        t-=1
        print('НЕ УГАДАЛ!! Попытайся еще!')
    let=let + let1
    if slovo=="_"*len(x1):
        print("Поздравляем! Вы выиграли, и на этот раз виселится останется без работы =(")
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
