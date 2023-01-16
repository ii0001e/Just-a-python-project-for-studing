from random import *
from sys import *
import keyboard


username_list = ["user1","user2","user3","user4"]
password_list = ["psw1","psw2","psw3","psw4"]
def password_generation(number_of_initials:int):
    """Parooli isegenereerimine
    Args:
        number_of_initials (int): _sümbolite arv_
    Returns:
        _type_: _tagastab uus parrol_
    """
    
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3 
    ls = list(str4)
    shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([choice(ls) for x in range(number_of_initials)])
    # Пароль готов
    print("Yours generated password is: ", psword)
    return psword

def user_choises(valik):
    """Funktsioon annab kasutajale valik: kas sisseloogida voi registreeruda
    """
    print("Hello! I'm yours helper! \n Please, make an accout or log in!")
    try:
        valik = int(input("If you want to make a new accout - enter number 1,\nif you want to log in - enter number 2\n--------> "))
    except:
        print("Enter the number!")
    if valik == 2:
        user_login()
    elif valik == 1:
        user_reg()
        user_login()
    user_log_out()
              
def user_login():
    """Funktsioon teeb sisselogimis protsessi
    """
    username = input("Please enter your username --> \n")
    try:
        if username in username_list:
            a = username_list.index(username)
            password = input("Please, enter the password --> \n")
            if password == password_list[a]:
                print("Log in succesfully!")
            else:
                print("Wrong password!")
        else:
            print("Worng username!")
    except:
        print("Error!")
              
def user_reg():
    """Kasutaja loob endale uus konto.
    Returns:
        _type_: tagastab password
    """
    username = input("Please, enter a new username --> \n")
    while username in username_list:
        print("This username in used! Please, choose the other one!")
        username = input("Please, enter a new username --> \n")
    else:    
        username_list.append(username)
    password = input("If you want to generate password - enter number 1,\nif you want to use yours password - enter number 2.\n ------> ")
    if password == "1":
        try:
            num = int(input("Enter the initials amount --> "))
        except:
            print("You must enter a number!")
        password_generation(num)
        password_list.append(password_generation(num))
    elif password == "2":
        while password_control(sala) == False:
            sala = input("Enter new password --> \n")
            password_control(sala)
        password_list.append(sala)
    return password
        
def password_control(password:str):
    """Func kontrollib salasona.
    Args:
        password (str): _salasona mis paneb ise kasutaja_
    Returns:
        _type_: return True or False.
    """
    password = list(password)

    num = len(password)
    k = 0
    l = 0
    o = 0
    for i in range(num):
        if password[i].isdigit():
            k += 1
        else:
            k += 0
        if password[i].isupper():
            l += 1
        else:
            l += 0
        if password[i].isalpha() == True:
            o += 1
        else:
            o += 0
    if k > 0 and l > 0 and o > 0:
        #print(True)
        return True
    else:
        print("Password must be consist of digits letters and capital letters!")
        return False

def user_log_out():
    """by press Enter or esc func continue or stop
    """
    print("Press Enter to continue or press Esc to exit: ")
    while True:
        if keyboard.is_pressed('ENTER'):
           print("you pressed Enter")
           user_choises(0)
        elif keyboard.is_pressed('Esc'):
           print("\nyou pressed Esc, so exiting...")
           exit()
    



user_choises(0)
