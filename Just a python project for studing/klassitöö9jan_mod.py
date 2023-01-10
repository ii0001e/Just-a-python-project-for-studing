from math import *
from datetime import *
def arithmetic(first_number:float,second_number:float,symbol:str) -> any:
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korratuamine, / jagamine
    Args:
        first_number (float): Esimene arv
        second_number (float): Teine arv
        symbol (str): Tehe 

    Returns:
        var: Määramata andmetüüp
    """
    if symbol in ["+","-","/","*"]:
        if symbol == "/" and second_number == 0:
            answer = "Div/0"
        else:
            answer = eval(str(first_number)+symbol+str(second_number))
    else:
        answer = "Tundmatu tehe!"
    return answer

def is_year_leap(year:int) -> str:
    """Liigaasta kalkulaator

    Args:
        year (int): year
    Returns:
        str: True/False
    """
    a = list(str(year))
    if len(a) == 4:
        if year % 4 == 0:
            answer = True
        else:
            answer = False
    else:
        answer = "Vale andmed"
    return answer

def square(square_wall:float) -> str:
    """Ruudu kalkulaator

    Args:
        square_wall (float): Ruudu laius/pikkus

    Returns:
        str: Pinge, Perimeeter, deagonaal
    """
    
    if square_wall > 0:
        P = 4 * square_wall
        S = square_wall ** 2
        D = sqrt(2)*square_wall
        answer = "Perimeeter - "+str(P)+", Pindala - "+str(S)+", Diagonaal - "+str(D)
    else:
        answer = "Andmed peavad olema suurem kui 0!"
    
    return answer

def season(month:int) -> str:
    """Aastaaeg

    Args:
        month (int): kuu number (1-12)

    Returns:
        str: Kevad, Suvi, Sügis, Talv
    """
    month = int(month)
    if month in range(1,13):
        if month in range(3,6):
            answer = "Kevad"
        elif month in range(6,9):
            answer = "Suvi"
        elif month in range(9,12):
            answer = "Sügis"
        else: 
            answer = "Talv"
    else:
        answer = "Vale kuu number!!"
    return answer

def bank(years:int, start_sum:float) -> str:

    """Protsenti kalkulaator

    Args:
        years (int): Mis perioodile
        start_sum (int): algsumma

    Returns:
        str: loppsumma
    """
    print(f"algsum {start_sum}")
    for i in range(1,int(years)+1):
        start_sum = start_sum * 1.1
    answer = "Lopsumma on " + str(round(start_sum,2))
    return answer

def is_prime(number:int)->any:
    """Lihtne arv

    Args:
        number (int): Number from 0 to 1000

    Returns:
        any: True / False
    """
    a = 0
    if number in range(0,1001):
        for i in range(2,(number//2 + 1 )):
            if (number % i == 0):
                a += 1
        if a <= 0:
            answer = True
        else:
            answer = False
    else:
        answer = "Out of range"
    return answer

def date(day:int,month:int,year:int) -> any:
    """Kuupäeva kontroll

    Args:
        day (int): Kuupäev
        month (int): Kuu
        year (int): Aasta

    Returns:
        any: True / False
    """
    try:
        if datetime(year,month,day):
            answer = True
        else:
            answer = False
    except:
        answer = "Vale andmed!"
    return answer

def XOR_code(code:str,password:str):
    """XOR code

    Args:
        code (str): Mingi sona
        password (int): teie parool

    Returns:
        str: kodeeritud sona
    """
    code = list(code)
    if str(password) == "12":
        unicode = hex
    elif str(password) == "123":
        unicode = bin
    elif str(password) == "12345":
        unicode = oct
    else:
        print("Wrong password!")
        
    for i in range(len(code)):
        code[i] = unicode(ord(code[i]))
    
#    print("Something goes wrong...")
    a = "".join(map(str,code))
    print("".join(map(str,code)))
    return a

def XOR_decode(code:str,password:str):
    """XOR code

    Args:
        code (str): Mingi sona
        password (int): teie parool

    Returns:
        str: kodeeritud sona
    """ 
    try:
        if str(password) == "12":
            unicode = 16
            code = list(code.split("0x"))
            for i in range(1,len(code)):
                code[i] = "0x"+code[i]
        elif str(password) == "123":
            unicode = 2
            code = list(code.split("0b"))
            for i in range(1,len(code)):
                code[i] = "0b"+code[i] 
        elif str(password) == "12345":
            unicode = 8
            code = list(code.split("0o"))
            for i in range(1,len(code)):
                code[i] = "0o"+code[i]
        else:
            print("Wrong password!")
        code.remove("")
        print(code)
        for i in range(len(code)):
            code[i] = chr(int(code[i], unicode))
        
    #    print("Something goes wrong...")
        a = "".join(map(str,code))
        print("".join(map(str,code)))
        return a
    except:
        print("Something goes wrong!")
    