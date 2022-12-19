def summ_controll(isikukood:str):
    """Isikukoodi kontroll number
    On vaja isikukood sisestada 
    :param str ik: inimese isikukood
    :trype: var Määramata tüüp
    """
    ik_list=list(isikukood)
    summa = 0
    summa_1 = 0
    ikoodid = []
    arvud = []
    for i in range(1,11):
        if i == 10:
            summa += 1 * int(ik_list[i-1])
        else:
            summa += i * int(ik_list[i-1])
    for i in range(1,11):
        if i in [1,2,3]:
            summa_1 += i * int(ik_list[i+6])
        else:
            summa_1 += i * int(ik_list[i-1])
    print("OK5")
    summa_jaak = summa // 11
    summa_jaak_1 = summa_1 // 11
    jaak = summa - (summa_jaak * 11)
    jaak_1 = summa_1 - (summa_jaak_1 * 11)
    if int(ik_list[10]) == jaak or int(ik_list[10]) == jaak_1:
        print("OK6")
        clinic_choise(isikukood)
        print("OK7")
        sugu(isikukood)
        print("OK8")
        vastus = "See on {sex}, tema sünnipäev on {datetime(age,month,day)} ja sünnikoht on {birth_place}"
        ikoodid.append(isikukood)
        print("OK9")
        return ikoodid
    else:
        print("OK10")
        vastus = "Viimane arv on vale!"
        arvud.append(isikukood)
        return arvud
    return vastus


def clinic_choise(isikukood:str):
    """Haigla 3 isikukoodi numbri alusel
    :param int ik3:
    :rtype: str Haigla ja koht
    """

    ik_list=list(isikukood)
    b = ik_list[7] + ik_list[8] + ik_list[9]
    if int(b) in range(1,11):
        birth_place = "Kuressaare Haigla"
    elif int(b) in range(11,21):
        birth_place = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif int(b) in range(21,221):
        birth_place = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif int(b) in range(221,271):
        birth_place = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif int(b) in range(271,371):
        birth_place = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif int(b) in range(371,321):
        birth_place = "Narva Haigla"
    elif int(b) in range(421,471):
        birth_place = "Pärnu Haigla"
    elif int(b) in range(471,491):
        birth_place = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif int(b) in range(491,521):
        birth_place = "Järvamaa Haigla (Paide)"
    elif int(b) in range(521,571):
        birth_place = "Rakvere, Tapa haigla"
    elif int(b) in range(571,601):
        birth_place = "Valga Haigla"
    elif int(b) in range(601,651):
        birth_place = "Viljandi Haigla"
    else:
        birth_place = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    return birth_place

def sugu(isikukood:str):
    
    ik_list=list(isikukood)
    if int(ik_list[0]) in [1,3,5]:
        sex = "Mees"
    else:
        sex = "Naine"
    return sex