from isikukood_mod import *

ik = input("Sisesta isikukoodi: ")
arvud = []
ikoodid = []
if len(ik) == 11:
    try:
        ik_list=list(ik)
        if int(ik_list[0]) in [1,2,3,4,5,6]:
            if mytime(ik):
                print(summ_controll(ik))
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
 