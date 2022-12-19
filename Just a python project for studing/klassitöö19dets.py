from datetime import datetime
from isikukood_mod import *

ik = input("Sisesta isikukoodi: ")
arvud = []
ikoodid = []
if len(ik) == 11:
    try:
        print("OK")
        ik_list=list(ik)
        if int(ik_list[0]) in [1,2,3,4,5,6]:
            print("OK2")
            if int(ik_list[0]) in [1,2]:
                a = 1800
            elif int(ik_list[0]) in [3,4]:
                a = 1900
            else:
                a = 2000
            age = a+int(ik_list[1]+ik_list[2])
            month = int(ik_list[3]+ik_list[4])
            day = int(ik_list[5]+ik_list[6])
            if datetime(age,month,day):
                print("OK3")
                summ_controll(ik)
                print(f"See on {sugu(ik)}, tema sünnipäev on {datetime(age,month,day)} ja sünnikoht on {clinic_choise(ik)}")
                print(ikoodid)
                print("OK4")
            else:
                print("Kuuaeg on valesti sisestatud!")
                arvud.append(ik)
                print(arvud)
        else:
            print("Esimene arv on vale!")
            arvud.append(ik)
            print(arvud)
    except:
        print("Andmete tüüp on vale, on vaja sisestada numbreid!")
        arvud.append(ik)
        print(arvud)
else:
    print("Sümbolite arv peab olema 11!")
    arvud.append(ik)
    print(arvud)
 