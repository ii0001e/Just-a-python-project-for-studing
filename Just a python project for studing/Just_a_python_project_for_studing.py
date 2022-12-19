from math import *

def test():
    a = float(input("Kõrgus: "))
    b = float(input("Laius: "))
    if a>0 and b>0: # and; or; not;  #==; !=; >=; <=
        S = a*b #*; /; +; -; //; %; **; d=e=4
    else:
        S="Ei saa leida"
    print("Pindala:", S)
#test()

def kusimus():
    a = int(input("Tere, kallikene!, mis hinne sa täna said?  "))
    if a >= 1 and a <= 5: 
        if a == 1:
            vastus = "Noh, kuidas nii! Mine kodutoo tegema!!!!"
        elif a == 2:
            vastus = "Aga ma utlesin sulle, et seda oli vaja teha!"
        elif a == 3:
            vastus = "Lahme teed juua..."
        elif a == 4:
            vastus = "Tore, aga sa võiks paremini teha!"
        else:
            vastus = "Kui tore! Mine ja võta pirakat laualt!"
    else:
        vastus = "Kallikene, ütle minule oma hinda!"
        kusimus()
    print(vastus)
#kusimus()

def zad1():
    #Задача  1
    # вводит число, программа определяет знак числа(положительное оно или отрицательное), если число положительное, то проверяет его на  четность и нечетность.
    a = input("Введи номер: ")
    if a.isalpha():
        print("See on tekst!!!")
    elif a.isdigit():
        a = int(a)
        if a>0:
            if a % 2 == 0:
                print(f"{a} - Четное")
            else:
                print(f"{a} - Нечетное")
        else:
            print(f"{a} - Отрицательное")
    else:
        print(f"{a} - смешанный тест с цифрами.")
#zad1()

def zad2():
    #Задача  2
    #Спросить у пользователя 3 числа, если они окажуться положительными, то проверить могут ли они быть углами одного треугольника(сумма углов 180) 
    #и уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).
    a = float(input("Укажи первый угол треугольника: "))
    b = float(input("Укажи второй угол треугольника: "))
    c = float(input("Укажи третий угол треугольника: "))
    if a>0 and b>0 and c>0:
        if a+b+c == 180:
            if a==90 or b ==90 or c==90:
                ugl = "Это углы прямоугольного и "
            elif a < 90 and b < 90 and c < 90:
                ugl = "Это углы остроугольного и "
            else:
                ugl = "Это углы тупоугольного и "
            if a == b == c == 60:
                stor = "равностороннего треугольника!"
            elif a == b or a == c or b==c:
                stor = "равнобедренного треугольника!"
            else:
                stor = "разностороннего треугольника!"
        else:
            print("Это не углы треугольника.")
    else:
        print("Неверные значения!")
    print(ugl, stor)
#zad2()

def zad3():
    #Задача  3
    #Выяснить у пользователя желание расшифровать порядковый номер дня недели в название. Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.

    question = input("Желаете ли расшифровать порядковый номер для недели? Да/Нет ")
    if question.isalpha():
        a = str(question.upper())
        if a=="ДА" or a =="DA":
            b = int(input("Укажите номер недели числом: "))
            if b>=1 and b<=7: 
                if b == 1:
                    num = "Понедельник"
                elif b == 2:
                    num = "Вторник"
                elif b == 3:
                    num = "Среда"
                elif b == 4:
                    num = "Четверг"
                elif b == 5:
                    num = "Пятница"
                elif b == 6:
                    num = "Суббота"
                else:
                    num = "Воскресенье"
            else:
                print("Число больше семи или меньше единицы!")
            print(num)
    else:
        print("Попытка не пытка....")
#zad3()

def zad4():
    #Задача  4

    #Определить по дню и месяцу рождения пользователя кто он по гороскопу. 
    #Проверять введенные данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение!
    den = input("Какого числа у вас день рождение? Укажите только день месяца! ")
    mes = input("В каком месяца у вас день рождение? Укажите номер месяца от 1 до 12! ")
    if den.isdigit() and mes.isdigit() and int(den)<=31 and int(mes)<=12 and int(den)>0 and int(mes)>0:
        den = int(den)
        mes = int(mes)
        list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сенябрь", "Октябрь", "Ноябрь", "Декабрь"]
        list_2 = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей Рыбы"]
        if mes == 2 and den>29:
            print("Неверная дата!")     
        else:
            pass
        a = list[mes-1]
        print(f"{den}", a, " - в этот день ваш день рождения.")
    else:
        print("Извините, где-то ошибка!") 
#zad4()

def zad5():
    #Задача (самостоятельно)
    #Проверить введенное пользователем число, отпределить его тип и если число целое, то найти от него 50%, если число дробное, 
    #то найти от него 70%, если это текст, то вывести его на экран. Для решения можно использовать: is_integer(), isalpha(), isdigit(), int(), float(), //, %.

    a = input("Введите любое число! ")
    try:
        a=int(a)
        answer=a*0.5
    except:
        try:
            a = float(a)
            answer = a*0.7
        except:
            answer = str(a)
    print(answer)
#zad5()

def zad6():
    #Задача  (самостоятельно)
    #Написать программу для решения квадратного уравнения a*x**2+b*x+c=0.
    #Спросить надо 3 значания: a, b, c.
    #Найти D: D=b**2-4ac.
    #Если D>0, то 2 решения,
    #если D=0, то 1 решение,
    #если D<0, то решений нет.
    #Ответы огруглить до 2 знаков после запятой.
    a = int(input("Sisesta a-väärtus: "))
    b = int(input("Sisesta b-väärtus: "))
    c = int(input("Sisesta c-väärtus: "))
    D = int(b**2-4*a*c)
    if D>0:
        x_1 = round((-b+sqrt(D))/(2*a),2)
        x_2 = round((-b-sqrt(D))/(2*a),2)
        print(x_1, x_2)
    elif D==0:
        x = round((-b+sqrt(D))/(2*a),2)
        print(x)
    else:
        print("Vastus puudub")
#zad6()

def massiind():
    print("Tere! Olen sinu uus sõber - Python!")
    nimi = str(input("Mis sinu nimi on? "))
    print(f"{nimi}, oi kui ilus nimi!")
    choose = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if choose == 1:
        try:
            pikkus = int(input("Sisesta oma pikkus CM-s. => "))
            while pikkus < 0 or pikkus > 273:
                print("Pikkus peab olema rohkem kui null ja vähem kui 273. Ja kirjutatud numbritega!")
                pikkus = input("Sesesta oma pikkus CM-s. => ")
        except:
            pikkus = 170
            print("Siis pikkus on 170 cm.")
        try:
            mass = float(input("Siseta oma keha kaal KG-s. => "))
            while mass < 0:
                print("Mass peab olema rohkem kui null!")
                mass = float(input("Sesesta oma pikkus KG-s. => "))
            else:
                pass
        except:
            mass = 69
            print("Siis teie mass on 69 kg.")
        index = round((mass / (0.01 * pikkus)**2), 1)
        print(f"{nimi}! Sinu keha indeks on: {index}")
        if index <= 16:
            answer = "Tervisele ohtlik alakaal"
        elif 16 < index <= 19:
            answer = "Alakaal"
        elif 19 < index <= 25:
            answer = "Normaalkaal"
        elif 25 < index <= 30:
            answer = "Ülekaal"
        elif 30 < index <= 35:
            answer = "Rasvumine"
        elif 35 < index <= 40:
            answer = "Tugev rasvumine"
        else:
            answer = "Tervisele ohtlik rasvumine"     
    else:
        answer = "Kahju! See on väga kasulik info!" + "\n"
    print (answer)
    print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
#massiind()