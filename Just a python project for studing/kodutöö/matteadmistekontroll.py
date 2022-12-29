from random import *
level_1 = ("+","-")
level_2 = ["+","-","/","*"]
level_3 = ["+","-","/","*","**"]

try:
    level_choise = int(input("Sisesta, millise raskusega ülesanned tahaksite tesitda? Sisata 1, 2 voi 3 --->   "))
    attempt = int(input("Mitu ülesannet sa tahad korrata: "))
except ValueError:
    print("Siseta ainult arv")

for i in range(attempt):
    if level_choise == 1:
        a = randint(1,100)
        b = randint(-100,100)
        c = choice(level_1)
        question = "{}{}{}".format(a,c,b)
        print(question)
        answer = input(f"Sisesta vastus: {a}{c}{b}  -->  ")
        print (answer)
        if int(answer) == eval(question):
            i += 1
            print("Oige!")
        else: 
            print("Vale!")
    elif level_choise == 2:
        a = randint(1,100)
        b = randint(1,100)
        c = choice(level_2)
        question = "{}{}{}".format(a,c,b)
        answer = input(f"Sisesta vastus: {a}{c}{b}  -->  ")
        if int(answer) == eval(question):
            i += 1
            print("Oige!")
        else: 
            print("Vale!")
    else:
        a = randint(1,100)
        b = randint(1,100)
        c = choice(level_3)
        question = "{}{}{}".format(a,c,b)
        answer = input(f"Sisesta vastus: {a}{c}{b}  -->  ")
from random import *
level_1 = ("+","-")
level_2 = ["+","-","/","*"]
level_3 = ["+","-","/","*","**"]

try:
    level_choise = int(input("Sisesta, millise raskusega ülesanned tahaksite tesitda? Sisata 1, 2 voi 3 --->   "))
    attempt = int(input("Mitu ülesannet sa tahad korrata: "))
except ValueError:
    print("Siseta ainult arv")

for i in range(attempt):
    if level_choise == 1:
        a = randint(1,100)
        b = randint(-100,100)
        c = choice(level_1)
        question = "{}{}{}".format(a,c,b)
        print(question)
        answer = input(f"Sisesta vastus: {a}{c}{b}  -->  ")
        print (answer)
        if int(answer) == eval(question):
            i += 1
            print("Oige!")
        else: 
            print("Vale!")
    elif level_choise == 2:
        a = randint(1,100)
        b = randint(1,100)
        c = choice(level_2)
        question = "{}{}{}".format(a,c,b)
        answer = input(f"Sisesta vastus: {a}{c}{b}  -->  ")
        if int(answer) == eval(question):
            i += 1
            print("Oige!")
        else: 
            print("Vale!")
    else:
        a = randint(1,100)
        b = randint(1,100)
        c = choice(level_3)
        question = "{}{}{}".format(a,c,b)
        answer = input(f"Sisesta vastus: {a}{c}{b}  -->  ")
        if int(answer) == eval(question):
            i += 1
            print("Oige!")
        else: 
            print("Vale!")

result = i / attempt * 100
if result > 90:
    print("Väga hea töö, sul on hinne --> '5'")
elif result in range(75,90):
    print("Hästi tehtud, sul on hinne '4'")
elif result in range(60,75):
    print("Hinne --> '3'")
else:
    print("Hinne --> '2'")
    