from random import *
from math import *
def zad1():
# Задание 1: Почтовый индекс
# В Эстонии почтовые индексы состоят из 5 чисел, где первое число обозначает уезд:

# Напишите программу, которая проверяет введенный индекс(количество символов, соответствие типу данных и т. д.) 
# и отображает уезд, к которому он относится. 
# Для проверки какому уезду принадлежит индекс, надо проверить первую цифру введенного значения. 
# Для этого введеный индекс надо преобразовать в список при помощи indeks_list=list(indeks) 
# и взять только первый элемент для проверки indeks_list[0].
# И если почтовый индеск Нарвы, Таллинна и Кохтла-Ярве, 
# то сообщить пользователю "Оставайтесь дома!", в остальных случаях "Носите маски!".
    index_town = ["Tallinn",
                    "Narva, Narva-Jõesuu",
                    "Kohtla-Järve",
                    "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
                    "Tartu linn",
                    "Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
                    "Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
                    "Pärnumaa",
                    "Läänemaa, Hiiumaa, Saaremaa"]

    try:
        index = input("Sisestage oma postiindex: ")
        index_list = list(index)
        if len(index_list) == 5:
            if int(index_list[0]) in range (1,10):
                n = int(index_list[0])
                print(f"Indeksi ala on {index_town[n-1]}")
                if n == 1 or n == 2 or n == 3:
                    print("Ole kodus!!!")
                else:
                    print("Kanna maski!")
            else:
                print("Vale indeks!")    
        else:
            print("Sisestatud arve ei ole index!")
    except:
        print("Andmetüüpi viga, on vaja sisestada postiindex arvuga.")
#zad1()

def zad2():

# Задание 2: Перемена мест
# Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). 
# Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.
    list = []
    try:
        a = int(input("Mitu elemendid soovite näha listis? \n"))
        while a < 3 or a > 15:
            print("Liiga lühike voi pikk list! \nPane miinimum 3 ja maaksimum 15 sümbolid!")
            a = int(input("Mitu elemendid soovite näha listis? \n"))
        n = int(input("Mitu korda tahate vahetada sümbolid? \n"))
        if a%2 == 0:
            n_max = a / 2
        else:
            n_max = a // 2
        while n_max > a:
            print("Ei saa vahetada rohkem korda nagu listis.")
            n = int(input("Mitu korda tahate vahetada sümbolid? \n"))
            
    except ValueError:
        print("Vale andmetüüb, sisesta ainult number!") 
        breakpoint  
    for x in range(1,a+1):
        list.append(x)
        x += 1
    print (f"Meie esialgne list on \n{list}")
    i = 0
    for i in range(n):
        list[i],list[-1-i] = list[-1-i],list[i]
        i += 1
    print(f"Meie loplik list on: \n {list}")
#zad2()


def zad3():
# Задание 3: Бесполезные числа
# Николай задумался о поиске «бесполезного» числа на основании списка. 
# Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, 
# а затем делит его на длину списка и заменяет его в списке результатом деления. 
# Студент пока не придумал, где может пригодиться подобное значение, 
# но ищет у вас помощи в реализации такой функции.
    list = []
    for x in range(1,randint(4,20)):
        list.append(randint(1,100))
        x += 1
    print(f"Meie list enne muutmist: \n{list}")
    a = list.index(max(list))
    division_of_number = round(max(list)/int(len(list)))
    list.remove(max(list))
    list.insert(a, division_of_number)
    print(f"Uuus list peale muutmist \n{list}")
#zad3()

def zad4():
# Задание 4: Сортировка
# Требуется создать программу, которая сортирует список чисел по убыванию/возрастанию их абсолютного значения.
    list_1 = []
    list = []
    for i in range(1,randint(4,12)):
        list_1.append(randint(-50,50))
        i += 1
    print(list_1)
    for x in range(len(list_1)):
        list.append(abs(list_1[x]))
        x += 1
    sorted(list,reverse=False)
    print(f"Kasvav list: \n{sorted(list, reverse = False)}")
    print(f"Kahanev list: \n{sorted(list, reverse = True)}")
#zad4()

def zad5():
# Задание 5: 
# На входе имеем список строк разной длины. 
    list_1 = ["крот", "белка", "выхухоль"]
    list_2 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
    list_3 = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
# Необходимо написать программу, которая вернет новый список из строк одинаковой длины. 
# Длину итоговой строки определяем исходя из самой большой из них. Если конкретная строка короче самой длинной, 
# дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов. 
# Расположение элементов начального списка не менять.
# ['крот____', 'белка___', 'выхухоль']
# ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
# ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']
    a = len(max(list_1,key=len))
    b = len(max(list_2,key=len))
    c = len(max(list_3,key=len))
    e = int(len(list_1))
    #g = int(a)
    print(a,e)
    for i in range(0,len(list_1)):
        word = list(list_1[i])
        if int(len(word)) <= int(a):
            list_1.pop(i)
            for x in range(0,int(a)-int(len(word))):
                word.extend("_")
            word_split = "".join(word,)
            list_1.insert(i,word_split)
        else:
            pass 
    print(list_1)
    for i in range(0,len(list_2)):
        word = list(list_2[i])
        if int(len(word)) <= int(b):
            list_2.pop(i)
            for x in range(0,int(b)-int(len(word))):
                word.extend("_")
            word_split = "".join(word,)
            list_2.insert(i,word_split)
        else:
            pass    
    print(list_2)
    for i in range(0,len(list_3)):
        word = list(list_3[i])
        if int(len(word)) <= int(c):
            list_3.pop(i)
            for x in range(0,int(c)-int(len(word))):
                word.extend("_")
            word_split = "".join(word,)
            list_3.insert(i,word_split)
        else:
            pass    
    print(list_3)    
#zad5()
